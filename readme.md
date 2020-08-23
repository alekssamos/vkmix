Python wrapper for [vkmix.com API](https://vkmix.com/settings/api). 
## Установка
`python3 -m pip install git+https://github.com/alekssamos/vkmix.git`
### Использование
```python3
from vkmix import VkMix

vkm = VkMix("YOURKEY")

print("Баланс: ", vkm.getBalance())

task = vkm.createTask(
	network = "vk",
	section = "likes",
	link = "https://vk.com/wall-139740824_2687166",
	count = 10,
	hourly_limit = 5,
	amount = 5
)
print("Создано задание: ID ", task["id"])

print("Получить все задания на аккаунте: ", vkm.getTasks())
```
## Runing tests
```bash
git clone https://github.com/alekssamos/vkmix.git

cd vkmix
python3 -m pip install -r requirements-dev.txt

python3 -m unittest
```
output:
 ```
....
----------------------------------------------------------------------
Ran 4 tests in 0.014s

OK

```
## Сборка
```bash
git clone https://github.com/alekssamos/vkmix.git
cd vkmix

python3 -m pip install --user --upgrade setuptools wheel

python3 setup.py build
python3 setup.py sdist bdist_wheel
```
