import pandas as pd

if __name__ == '__main__':
    prd = pd.read_excel("momo_product.xlsx", index_col=0)
    for i in prd.index:
        if prd.at[i, "price"] < 30000:
            prd = prd.drop(index=[i])
    prd.to_excel("momo_product_result.xlsx")