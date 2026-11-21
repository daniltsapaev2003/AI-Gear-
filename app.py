import os

from flask import Flask, abort, redirect, render_template, request, session, url_for

from data import CATEGORIES, PRODUCTS, find_product

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")


def cart_items():
    items = []
    for pid, qty in session.get("cart", {}).items():
        product = find_product(pid)
        if product:
            items.append({"product": product, "qty": qty, "sum": product["price"] * qty})
    return items


def cart_total():
    return sum(item["sum"] for item in cart_items())


@app.context_processor
def inject_globals():
    return {
        "categories": CATEGORIES,
        "cart_count": sum(session.get("cart", {}).values()),
    }


@app.route("/")
def index():
    hits = [p for p in PRODUCTS if p.get("hit")]
    return render_template("index.html", products=hits)


@app.route("/catalog/<slug>")
def catalog(slug):
    category = next((c for c in CATEGORIES if c["slug"] == slug), None)
    if category is None:
        abort(404)
    items = [p for p in PRODUCTS if p["category"] == slug]
    return render_template("catalog.html", category=category, products=items)


@app.route("/product/<pid>")
def product(pid):
    item = find_product(pid)
    if item is None:
        abort(404)
    return render_template("product.html", product=item)


@app.route("/cart")
def cart():
    return render_template("cart.html", items=cart_items(), total=cart_total())


@app.post("/cart/add/<pid>")
def cart_add(pid):
    if find_product(pid) is None:
        abort(404)
    cart = session.get("cart", {})
    cart[pid] = cart.get(pid, 0) + 1
    session["cart"] = cart
    return redirect(request.referrer or url_for("cart"))


@app.post("/cart/remove/<pid>")
def cart_remove(pid):
    cart = session.get("cart", {})
    cart.pop(pid, None)
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/search")
def search():
    q = request.args.get("q", "").strip().lower()
    results = [p for p in PRODUCTS if q and q in p["name"].lower()]
    return render_template("search.html", query=q, products=results)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
