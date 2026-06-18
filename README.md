# Django Zero to Hero 🚀

Welcome to my **Django Zero to Hero** learning journey! In this repository, I document my progress, notes, code snippets, and bug resolutions as I build, experiment, and master Django.

---

## 📅 Learning Log & Journal

### Day 1: Django Foundations & Routing
* **Topics Studied:**
  - Setting up a Django project structure (`core` project and `catalog` app).
  - Understanding **URL routing** using `urls.py` (both project-level and app-level using `include()`).
  - Creating **Views** in `views.py` (`HttpResponse` vs `render()` templates).
  - **Named URL patterns** (`name='home'`) and why they are used to avoid hardcoded URLs.
  - Passing data to HTML using **context dictionaries** (`context = {}`) and loop logic in templates (`{% for product in products %}`).

---

## 🐛 Bug Resolution Log

Here are the bugs encountered today and how we resolved them:

### 1. Django `ImproperlyConfigured` Error
* **Symptom:** 
  `ImproperlyConfigured: The included URLconf 'catalog.urls' does not appear to have any patterns in it.`
* **Cause:** 
  The routing list in `catalog/urls.py` was mistakenly named `URLPattern = [...]` instead of **`urlpatterns = [...]`** (lowercase, plural), which is Django's strict naming convention.
* **Resolution:**
  Rename `URLPattern` to `urlpatterns` and remove the unnecessary import of `from django.urls import URLPattern`.

### 2. `ModuleNotFoundError: No module named 'django.catalog'` (or `djnago`)
* **Symptom:** 
  Django failed to start with a traceback pointing to a missing module.
* **Cause:** 
  An invalid import statement `from django import catalog` was written at the top of `views.py`. `catalog` is a local app, not an internal module of the `django` library package.
* **Resolution:**
  Remove the invalid import. The views inside `catalog/views.py` do not need to import the `catalog` package.

### 3. Template Context Mismatch (Empty list rendering)
* **Symptom:** 
  The HTML template loaded but the list of products was empty.
* **Cause:** 
  - The context dictionary in `views.py` passed `'product': product_list`, but the template looked for `{% for product in products %}` (plural).
  - The context was also not being passed into the `render()` call.
* **Resolution:**
  - Rename the context key to `'products'`.
  - Pass the `context` variable as the third parameter in the render call: `render(request, 'catalog/product.html', context)`.

---

## 🛠️ How to Run Locally

1. Activate virtual environment:
   ```bash
   cd djnago
   venv\Scripts\activate
   ```
2. Run the development server:
   ```bash
   python manage.py runserver
   ```
3. Visit [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/) in your browser.
