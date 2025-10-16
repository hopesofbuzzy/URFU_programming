# Тестировани
# Учтите, что при каждом запуске блока будет добавляться всё больше и больше предметов

add(goods, "Молоко", 1, "2025-10-12")
add_by_note(goods, "Молоко 1 2025-10-13")
add_by_note(goods, "Молоко 1")
add_by_note(goods, "Яйца куриные 10 2025-09-29")
add_by_note(goods, "Яйца гусиные 10")

print(find(goods, "йц"))
print(amount(goods, "яйца куриные"))
print(goods)
