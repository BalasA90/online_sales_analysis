
from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()

     # Produse disponibile
    manager.add_product(Product("Canapea", 2900, 25))
    manager.add_product(Product("Pat", 4300, 9))
    manager.add_product(Product("Fotoliu", 550, 19))

     # Instanță coș
    cart = Cart()

    # Adăugăm 3 produse random
    cart.add_to_cart(manager.products[0])
    cart.add_to_cart(manager.products[1])
    cart.add_to_cart(manager.products[2])

    # Afișăm coșul
    cart.show_cart()
    print("Valoarea totală a coșului:", cart.total_cart_value(), "RON")
