
from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()

    # Adăugăm produse
    manager.add_product(Product("Dulap", 2900, 25))
    manager.add_product(Product("Pat", 3300, 9))
    manager.add_product(Product("Fotoliu", 550, 39))

    # Afișăm produse
    manager.show_products()

    # Valoarea totală
    print("Valoarea totală a inventarului:", manager.total_inventory_value(), "RON")