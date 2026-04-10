"""
Sample data fixture loader for Ambika Mahavidyalaya.
Run: python manage.py runscript load_sample_data
Or:  python manage.py shell < scripts/load_sample_data.py
"""

import os, sys, django

# Setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ambika.settings.local")
django.setup()

from apps.school.models import (
    HeroSlide, NewsPost, GalleryCategory, Facility,
    AcademicSubject, AdmissionInfo, StaffMember
)

# ── Facilities ──────────────────────────────────────
facilities_data = [
    ("📚", "Library / ગ્રંthala&#x200D;y", "Saraswati Pustakalaya", "A rich collection of Sanskrit scriptures, textbooks, and reference books."),
    ("🏠", "Hostel / Chhat&#x200D;ravas", "Rishi Kumar Chhatravas", "Comfortable residential facility with vegetarian meals, study rooms, and morning prayers."),
    ("🏫", "Classrooms / Vargkh&#x200D;andh&#x200D;s", "Aadarsh Vargkhand", "Spacious, well-ventilated classrooms equipped with blackboards and modern teaching aids."),
    ("⚽", "Sports Ground / Rme&#x200D;dan", "Krida Maidan", "Open ground for kabbadi, cricket, and yoga activities."),
    ("🕉️", "Prayer Hall / Puja&#x200D;khanda", "Aaradhana Kaksham", "Daily morning and evening prayers and Sanskrit shloka recitation."),
    ("🍽️", "Dining Hall / Bho&#x200D;jansha&#x200D;la", "Anna Purna Bhojanshala", "Clean, hygienic dining hall serving nutritious Satvik vegetarian meals."),
    ("🌳", "Peaceful Campus", "Prasanta Parisar", "Serene green campus within the sacred Ambaji temple town."),
    ("💊", "Medical Room", "Swasthya Kaksha", "First aid and medical assistance facility on campus."),
]

print("Creating facilities...")
for icon, name_gu, name_en, desc_en in facilities_data:
    obj, created = Facility.objects.get_or_create(icon=icon)
    obj.set_current_language("en")
    obj.name = name_en
    obj.description = desc_en
    obj.save()
    obj.set_current_language("gu")
    obj.name = name_gu
    obj.description = desc_en  # fallback
    obj.save()
    print(f"  {'[NEW]' if created else '[OK]'} {name_en}")

# ── Academic Subjects ────────────────────────────────
print("\nCreating academic subjects...")
subjects = [
    ("9",  "Sanskrit / સars&#x200D;krit", "Sanskrit",             "Core Sanskrit language, grammar, and literature"),
    ("9",  "Mathematics / Gan&#x200D;it",   "Mathematics",          "Algebra, Geometry, Arithmetic"),
    ("9",  "Science / Vigya&#x200D;n",      "Science",              "Physics, Chemistry, Biology"),
    ("9",  "Gujarati / Guj&#x200D;arat&#x200D;i", "Gujarati",      "Gujarati language and literature"),
    ("9",  "Social Science / Sa&#x200D;ma&#x200D;jik", "Social Studies", "History, Geography, Civics"),
    ("9",  "Hindi / Hin&#x200D;di",         "Hindi",                "Hindi language basics"),
    ("9",  "Dharma / Dha&#x200D;rm",        "Dharma & Culture",     "Indian culture, values, Sanskrit slokas"),
    ("11", "Sanskrit (Adv) / Sanskrit", "Sanskrit Advanced",    "Advanced Sanskrit prose, poetry, grammar"),
    ("11", "Mathematics / Gan&#x200D;it",   "Mathematics",          "Higher algebra, calculus basics"),
    ("11", "Gujarati / Guj&#x200D;arat&#x200D;i", "Gujarati",      "Higher Gujarati language"),
    ("11", "Hindi / Hin&#x200D;di",         "Hindi",                "Higher Hindi"),
    ("11", "Dharma / Dha&#x200D;rm",        "Dharma & Philosophy",  "Vedic philosophy, ethics"),
    ("11", "English / Ang&#x200D;rezi",     "English",              "Basic English communication"),
]

for i, (std, name_gu, name_en, desc) in enumerate(subjects):
    obj, created = AcademicSubject.objects.get_or_create(standard=std, order=i)
    obj.set_current_language("en")
    obj.name = name_en
    obj.description = desc
    obj.save()
    obj.set_current_language("gu")
    obj.name = name_gu
    obj.description = desc
    obj.save()
    print(f"  {'[NEW]' if created else '[OK]'} Std {std}: {name_en}")

# ── Admission Info ────────────────────────────────────
print("\nCreating admission info...")
admissions = [
    ("9",  
     "Passed Std-8 from a recognized school. Boys only (Rishi Kumars). Minimum 50% marks preferred.",
     "Passed Std-8 from a recognized school. Boys only (Rishi Kumars). Minimum 50% marks preferred.",
     "Contact school for fee details: +91 9925368974",
     "Contact school for fee details: +91 9925368974",
    ),
    ("11",
     "Passed Std-10 (SSC) from GSEB or equivalent board. Boys only. Science or Arts stream available.",
     "Passed Std-10 (SSC) from GSEB or equivalent board. Boys only. Science or Arts stream available.",
     "Contact school for fee details: +91 9925368974",
     "Contact school for fee details: +91 9925368974",
    ),
]

for std, eli_en, eli_gu, fee_en, fee_gu in admissions:
    obj, created = AdmissionInfo.objects.get_or_create(standard=std)
    obj.academic_year = "2026-27"
    obj.is_open = True
    obj.set_current_language("en")
    obj.eligibility = eli_en
    obj.fees_details = fee_en
    obj.process = "1. Fill the application form\n2. Submit required documents\n3. Attend interview\n4. Pay fees and confirm admission"
    obj.notes = "Hostel facility available. Contact school for details."
    obj.save()
    obj.set_current_language("gu")
    obj.eligibility = eli_gu
    obj.fees_details = fee_gu
    obj.save()
    print(f"  {'[NEW]' if created else '[OK]'} Std {std}")

# ── News Posts ────────────────────────────────────────
print("\nCreating sample news posts...")
news_data = [
    (
        "Shri Ambika Mahavidyalaya Admission Open 2026-27",
        "ambika-admission-2026-27",
        "Admissions are now open for Std-9 and Std-11 for academic year 2026-27.",
        "Shri Ambika Sanskrit Mahavidyalaya, Ambaji is pleased to announce that admissions are open for Standard 9 and Standard 11 for the academic year 2026-27. Eligible Rishi Kumars (Boys) are invited to apply. For more information, contact: 9925368974 or email: shriambika1@gmail.com",
        True,
    ),
    (
        "Annual Sanskrit Day Celebration",
        "sanskrit-day-celebration",
        "The school celebrated Sanskrit Day with great enthusiasm and cultural programs.",
        "The annual Sanskrit Day was celebrated with great devotion and enthusiasm at Shri Ambika Sanskrit Mahavidyalaya. Students performed Sanskrit shlokas, plays, and cultural programs. The event was graced by the presence of senior trust members and scholars.",
        False,
    ),
    (
        "Annual Prize Distribution Ceremony",
        "annual-prize-distribution",
        "The annual prize distribution ceremony was held with great pomp.",
        "The annual prize distribution ceremony was held at the school campus. Outstanding students were felicitated with prizes for academic excellence, Sanskrit recitation, and extracurricular achievements. The event was chaired by the trust president.",
        False,
    ),
]

for title, slug, excerpt, body, featured in news_data:
    obj, created = NewsPost.objects.get_or_create(translations__slug=slug) if NewsPost.objects.filter(translations__slug=slug).exists() else (NewsPost.objects.create(), True)
    obj.is_published = True
    obj.is_featured = featured
    obj.set_current_language("en")
    obj.title = title
    obj.slug = slug
    obj.excerpt = excerpt
    obj.body = body
    obj.save()
    obj.set_current_language("gu")
    obj.title = title + " (ગujarati)"
    obj.slug = slug + "-gu"
    obj.excerpt = excerpt
    obj.body = body
    obj.save()
    print(f"  {'[NEW]' if created else '[OK]'} {title}")

print("\n✅ Sample data loaded successfully!")
print("Visit http://localhost:8000/ to see the website.")
print("Admin: http://localhost:8000/admin/")
