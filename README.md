# 🛕 શ્રી અંબિકા સંસ્કૃત મહાવિદ્યાલય, અંબાજી
## Shri Ambika Sanskrit Mahavidyalaya, Ambaji

**Managed by:** શ્રી આરાસુરી અંબાજી માતા દેવસ્થાન ટ્રસ્ટ  
**Tagline:** Sanskrit Education for Rishi Kumars (Boys) – Std 9 to 12  
**Phone:** 9925368974 | **Email:** shriambika1@gmail.com  

---

## 📋 Tech Stack

| Layer | Technology |
|---|---|
| Backend | **Python Django 5.x** + **django-cms 4.x** |
| Templates | **Jinja2** (via django-jinja) |
| Styling | **Tailwind CSS 3.x** (saffron/gold theme) |
| Database | **SQLite** (local) / **PostgreSQL** (production) |
| i18n | **django-parler** (Gujarati ↔ English, no API) |
| Container | **Docker** + **docker-compose** |
| Files | **django-filer** with easy-thumbnails |

---

## 🚀 Local Setup (Step-by-Step)

### Prerequisites
- Python 3.11+
- Git

### 1. Clone and enter the project
```bash
cd /Users/nitesh/Desktop/projects/djangocms
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Build Tailwind CSS
```bash
python manage.py tailwind build
```
> **During development**, run `python manage.py tailwind watch` in a separate terminal to watch for changes.

### 5. Run database migrations
```bash
python manage.py migrate
```

### 6. Compile locale files
```bash
python manage.py compilemessages
```

### 7. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
> Enter username, email, and password when prompted.

### 8. Load sample content (optional but recommended)
```bash
python scripts/load_sample_data.py
```

### 9. Collect static files (for production only)
```bash
python manage.py collectstatic
```

### 10. Run the development server
```bash
python manage.py runserver
```

**Visit:** http://127.0.0.1:8000/  
**Admin:** http://127.0.0.1:8000/admin/

---

## 🌐 Language Switcher

The website supports **Gujarati** (default) and **English**.

- Gujarati URL: `http://localhost:8000/` or `http://localhost:8000/gu/`
- English URL: `http://localhost:8000/en/`

The language switcher buttons (**ગુ | EN**) are always visible in the header.

---

## ✏️ Adding Content in Both Languages

### 1. CMS Pages (via CMS toolbar)
1. Log in as admin
2. Navigate to any page
3. Click **Edit** in the CMS toolbar
4. Add/edit plugins (Text, Images, etc.)
5. Switch language using the language switcher
6. Repeat for the other language
7. Click **Publish**

### 2. News Posts
1. Go to Admin → **School → News Posts**
2. Click **Add News Post**
3. Fill in **English** fields (select "English" tab)
4. Switch to **Gujarati** tab and fill Gujarati fields
5. Check **Published** and **Featured** as needed
6. Save

### 3. Gallery
1. Admin → **School → Gallery Categories** → Add category (both languages)
2. Admin → **School → Gallery Items** → Add image with caption

### 4. Hero Slides
1. Admin → **School → Hero Slides**
2. Add title, subtitle, button text in both languages
3. Upload the hero image
4. Set order and mark as **Active**

### 5. Staff Members
1. Admin → **School → Staff Members**
2. Add name and designation in both languages
3. Upload photo

### 6. Admission Info
1. Admin → **School → Admission Info**
2. Edit Std 9 and Std 11 records
3. Fill eligibility, fees, process in both languages

---

## 📄 CMS Pages Setup (First Time)

After running the server, go to **Admin → CMS → Pages** and create:

| Page Title | Template | Slug |
|---|---|---|
| Home | `home.html` | `/` |
| About Us | `about.html` | `/about/` |
| Academics | `academics.html` | `/academics/` |
| Admissions | `admissions.html` | `/admissions/` |
| Gallery | `gallery.html` | `/gallery/` |
| News | `news/list.html` | `/news/` |
| Facilities | `facilities.html` | `/facilities/` |
| Contact | `contact.html` | `/contact/` |

For each page:
1. Create in **Gujarati** first (default language)
2. Add the **Gujarati** slug and title
3. Switch to **English** and add English title and content

---

## 🔧 Adding New Plugins

To add a new CMS plugin:

1. **Create the plugin model** (if it needs to store data) in `apps/school/models.py`
2. **Register the plugin** in `apps/school/cms_plugins.py`:

```python
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

@plugin_pool.register_plugin
class MyNewPlugin(CMSPluginBase):
    name = "My New Plugin"
    render_template = "cms/plugins/my_new_plugin.html"
    
    def render(self, context, instance, placeholder):
        context["my_data"] = MyModel.objects.all()
        return context
```

3. **Create the template** at `templates/cms/plugins/my_new_plugin.html`
4. Run `python manage.py migrate` if you added a new model
5. The plugin will appear in the CMS toolbar under "Structure"

---

## 🐳 Docker Setup

### Build and run with Docker Compose (PostgreSQL):
```bash
docker-compose up --build
```

### Run migrations inside container:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py compilemessages
```

### Access:
- Website: http://localhost:8000
- Admin: http://localhost:8000/admin/

---

## 📁 Project Structure

```
djangocms/
├── ambika/                  # Django project
│   ├── settings/
│   │   ├── base.py          # Shared settings
│   │   ├── local.py         # Dev (SQLite)
│   │   └── production.py    # Prod (PostgreSQL)
│   ├── jinja2.py            # Jinja2 environment
│   └── urls.py
├── apps/
│   ├── school/              # School models, admin, CMS plugins
│   └── contact/             # Contact form
├── templates/               # Jinja2 templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── academics.html
│   ├── admissions.html
│   ├── gallery.html
│   ├── news/
│   ├── facilities.html
│   ├── contact.html
│   └── cms/plugins/         # CMS plugin templates
├── static/
│   ├── src/input.css        # Tailwind source
│   ├── dist/output.css      # Compiled Tailwind
│   └── js/main.js
├── locale/
│   ├── en/LC_MESSAGES/      # English translations
│   └── gu/LC_MESSAGES/      # Gujarati translations
├── scripts/
│   └── load_sample_data.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── tailwind.config.js
├── package.json
└── manage.py
```

---

## 🎨 Design System

Colors:
- **Saffron** `#FF9800` – Primary action color
- **Gold** `#D4AF37` – Accent / decorative
- **Cream** `#FFF8E7` – Background
- **Maroon** `#7B1A1A` – Headings
- **White** – Cards and content areas

Fonts:
- `Yatra One` – Display headings
- `Noto Serif Gujarati` – Gujarati content
- `Noto Sans Gujarati` – Body text
- `Inter` – English body text

---

## 📞 School Contact

```
શ્રી અંબિકા સંસ્કૃત મહાવિદ્યાલય, અંબાજી
Shri Ambika Sanskrit Mahavidyalaya, Ambaji

Phone:  +91 9925368974
Email:  shriambika1@gmail.com
Place:  Ambaji, Banaskantha, Gujarat – 385110

Managed by: શ્રી આરાસુરી અંબાજી માતા દેવસ્થાન ટ્રસ્ટ
```

---

*ॐ — Designed for the digital presence of a sacred Sanskrit institution.*
