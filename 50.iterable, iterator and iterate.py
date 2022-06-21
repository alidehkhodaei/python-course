# iterable
# هر آبجکتی که قابلیت تبدیل شدن به ایتریتور رو دارد مثل لیست ها، ست ها و...

# iterator
# هر آبجکتی که می توانیم روی آیتم هاش پیمایش کنیم.

# iterate
# به هر پیمایش، iterate گفته میشود.

#----------------------------

items = [1, 2, 3, 4, 5] # iterable

iter_items = iter(items) # iterator

print(iter_items)  # <list_iterator object at 0x000001FAB05FA2F0>

print(next(iter_items))
print(next(iter_items))
print(next(iter_items))
print(next(iter_items))
print(next(iter_items))

#----------------------------

for item in items:
  print(item)

  '''
  for در حلقه
 iterable وقتی یک  
 iterator بهش میدیم خودش تیدیل به
iter() میکنه با استفاده از
 را روش فراخونی میکنه next و
'''

