# Journal Log: Day 1

**Date:** June 18, 2026

## 📚 What I Studied Today

1. **Django Project & App Setup:**
   - Created a main Django project named `core`.
   - Created an app named `catalog` to handle views, models, and template rendering for products.
   - Initialized a Python virtual environment (`venv`) to keep package dependencies isolated.

2. **Routing (URLs) Architecture:**
   - Learned how the root `urls.py` in the `core` folder delegates paths using Django's `include()` function.
   - Connected `path('', include('catalog.urls'))` so that the `catalog` app's custom urls handle matching requests.
   - Used named URL patterns (e.g. `name='home'`, `name='product'`) to dynamic-link pages without hardcoding URL paths like `/products/` directly in the HTML.

3. **Views & Responses:**
   - Created views returning raw HTML text using `HttpResponse`.
   - Created templates using standard HTML and used `render()` to tie views and templates together cleanly.

4. **Passing Context Data to Templates:**
   - Learned how a python dictionary `context` is passed from the view to the HTML template.
   - Displayed dynamic data (a list of products) in HTML using Django's template engine:
     ```html
     {% for product in products %}
         <li>{{ product }}</li>
     {% endfor %}
     ```

---

## 🐛 Bugs Resolved

### 1. `ImproperlyConfigured: The included URLconf 'catalog.urls' does not appear to have any patterns in it.`
* **Trigger:** Attempting to run the server or check the setup.
* **Why it happened:** In `catalog/urls.py`, the routing list variable was named `URLPattern` instead of the required lowercase name **`urlpatterns`**.
* **Fix:** Renamed the variable to `urlpatterns = [...]` and removed the unused `URLPattern` import.

### 2. `ModuleNotFoundError: No module named 'django.catalog'` (or `djnago`)
* **Trigger:** Server reload/startup crash.
* **Why it happened:** Wrote an invalid import `from django import catalog` inside `catalog/views.py`. Since `catalog` is a local app and not a module inside the Django framework, Python threw an error.
* **Fix:** Removed the invalid import since local views do not need to import their own app wrapper.

### 3. Products list displaying empty
* **Trigger:** Visiting the `/products/` page.
* **Why it happened:** 
  1. The dictionary key in the view context was named `'product'` (singular) but the template looped over `'products'` (plural).
  2. The `context` dictionary was not passed to `render(request, 'catalog/product.html')`.
* **Fix:** Updated the context key to `'products'` and passed `context` as the third argument in the `render` function:
  ```python
  return render(request, 'catalog/product.html', context)
  ```
