def linear_Search_Product(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["apple","orange","mango","apple","banana","apple","mango"]
print("Products:",products)
target = str(input("Enter target product name:"))
result = linear_Search_Product(products, target)
print(result)
