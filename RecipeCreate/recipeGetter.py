import getRecipeLink

def getHTML(ingredients):
    url = 'https://recipeland.com/recipes/list?q='
    full_url = url + getRecipeLink.getLink(ingredients)
    return full_url
