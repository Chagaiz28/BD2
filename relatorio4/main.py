from database import Database
from helper.writeAJson import writeAJson
from ProductAnalyzer import ProductAnalyzer


def main():
    db = Database(database="mercado", collection="compras")
    db.resetDatabase()

    analyzer = ProductAnalyzer(db.collection)

    analyzer.total_sales_per_day()
    analyzer.most_sold_product()
    analyzer.highest_spending_customer()
    analyzer.products_sold_above_one()


if __name__ == "__main__":
    main()
