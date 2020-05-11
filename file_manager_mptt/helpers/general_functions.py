## From https://www.geeksforgeeks.org/add-the-slug-field-inside-django-model/

from django.template.defaultfilters import slugify
import string, random 

def random_string_generator(size=10): 
    chars = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(size)) 

def unique_slug_generator(instance, new_slug=None): 
    if new_slug is not None: 
        slug = new_slug 
    elif instance.slug: 
        slug = instance.slug 
    else:
        slug = random_string_generator()
        
    _class = instance.__class__ 
    slug_exists = _class.objects.filter(slug=slug).exists() 
      
    if slug_exists: 
        randstr = random_string_generator(size=random.randint(8,15))
        new_slug = f"{slug}-{randstr}"
        return unique_slug_generator(instance, new_slug=new_slug) 

    return slug

