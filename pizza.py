import click
import random


def recipe_menu(pizza):
    """Готовит рецепт для вывода в меню"""
    result = ''
    result += pizza.name + ': '
    for i in range(len(pizza.recipe)):
        result += pizza.recipe[i]
        if i != len(pizza.recipe) - 1:
            result += ', '
    return result


class Margherita:
    def __init__(self, size='l'):
        self.name = 'Margherita'
        self.size = size.lower()
        self.recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
        if self.size != 'l' and self.size != 'xl':
            raise ValueError('Данный размер отсутствует.')

    def __dict__(self):
        d = {f'{self.name} 🧀': self.recipe}
        print(f'{d}')

    def __eq__(self, other):
        if isinstance(other, Margherita):
            return self.size == other.size
        else:
            return False


class Pepperoni:
    def __init__(self, size='l'):
        self.name = 'Pepperoni'
        self.size = size.lower()
        self.recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
        if self.size != 'l' and self.size != 'xl':
            raise ValueError('Данный размер отсутствует.')

    def __dict__(self):
        d = {f'{self.name} 🍕': self.recipe}
        print(f'{d}')

    def __eq__(self, other):
        if isinstance(other, Pepperoni):
            return self.size == other.size
        else:
            return False


class Hawaiian:
    def __init__(self, size='l'):
        self.name = 'Hawaiian'
        self.size = size.lower()
        self.recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        if self.size != 'l' and self.size != 'xl':
            raise ValueError('Данный размер отсутствует.')

    def __dict__(self):
        d = {f'{self.name} 🍍': self.recipe}
        print(f'{d}')

    def __eq__(self, other):
        if isinstance(other, Hawaiian):
            return self.size == other.size
        else:
            return False


def log(text):
    """В text вставляет время"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            time_order = random.randint(1, 600)
            print(text.format(str(time_order)))
            return result
        return wrapper
    return decorator


@log('Приготовили за {} c!')
def bake(pizza):
    print(f'Ваш заказ: пицца {pizza.name}')


@log('Доставили за {} c!')
def delivery_pizza(pizza):
    print(f'Горячая пицца {pizza.name} готова специально для Вас!')


@log('Забрали за {} c!')
def pickup(pizza):
    print(f'Горячая пицца {pizza.name} готова специально для Вас!')


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if pizza.lower() == 'hawaiian':
        bake(Hawaiian())
    elif pizza.lower() == 'pepperoni':
        bake(Pepperoni())
    elif pizza.lower() == 'margherita':
        bake(Margherita())
    else:
        click.echo('Данная пицца отсутствует в нашем меню.')
    if delivery:
        delivery_pizza(Hawaiian())
    else:
        pickup(Hawaiian())


@cli.command()
def menu():
    """Выводит меню"""
    click.echo(recipe_menu(Margherita()))
    click.echo(recipe_menu(Pepperoni()))
    click.echo(recipe_menu(Hawaiian()))


if __name__ == '__main__':
    cli()
