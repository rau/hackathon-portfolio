def getLink(ingredients):
    link = ''
    for ingredient in ingredients:
        if ' ' in ingredient:
            ingredient = ingredient[ingredient.find(" ") + 1:]
        ingredient = ingredient + '+'
        link = link + ingredient
    link = link[:-1]
    return link
