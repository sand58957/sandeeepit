import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Import models
from apps.about.models import aboutPage, teamSection, aboutPageSEO
from apps.home.models import (
    sliderSection, serviceSection, aboutSection, funFactSection, 
    projectCategory, projectSection, clientSection, testimonialsSection,
    homePageSEO, blogSectionTitle, clientSectionTitle, funfactSectionTitle,
    pricingSectionTitle, projectSectionTitle, teamSectionTitle, 
    testimonialSectionTitle, serviceSectionTitle
)
from apps.blog.models import blogCategory, Blogs, blogPageSEO
from apps.settings.models import websiteSetting, SeoSetting, headerFooterSetting
from apps.contact.models import ContactFormTitle, SubscriberFormTitle, contactPageSEO
from apps.pricing.models import pricingSection, pricingPageSEO
from apps.menus.models import primaryMenu

print("Loading sample data...")

# About Page
aboutPage.objects.get_or_create(id=1, defaults={
    'subtitle': 'Why Choose',
    'title': 'Phasellus Tristique A Nisi Etal Tristique Cras Interdum.',
    'description': 'Integer purus odio, placerat nec rhoncus in, ullamcorper nec dolor. Class online aptent taciti sociosqu ad litora torquent per conubia nostra.',
    'feature1': '24/7 Support',
    'feature2': 'Unique Design',
    'feature3': 'Clean Code Develop',
    'years_of_experience': 20,
})
print("✓ About Page created")

# About Page SEO
aboutPageSEO.objects.get_or_create(id=1, defaults={
    'meta_title': 'About Us',
    'meta_description': 'TCG Agency - About Us Page',
})
print("✓ About Page SEO created")

# Team Section
teamSection.objects.get_or_create(id=1, defaults={'name': 'Thoren Okendhild', 'position': 'Founder & Director'})
teamSection.objects.get_or_create(id=2, defaults={'name': 'Lincoln Anthony', 'position': 'Co Founder & CEO'})
teamSection.objects.get_or_create(id=3, defaults={'name': 'Adrian Eodri', 'position': 'Managing Director'})
print("✓ Team Section created")

# Slider Section
sliderSection.objects.get_or_create(id=1, defaults={
    'subtitle': 'Welcome to Agency',
    'title': 'Creative Digital Agency',
    'description': 'We create amazing digital experiences that help businesses grow and succeed in the digital world.',
    'button1_text': 'Get Started',
    'button1_url': '/contact',
    'button2_text': 'Learn More',
    'button2_url': '/about',
})
print("✓ Slider Section created")

# About Section
aboutSection.objects.get_or_create(id=1, defaults={
    'subtitle': 'About Us',
    'title': 'We Are Digital Agency',
    'short_description': 'Professional web design and development services for your business.',
    'long_description': 'We are a creative digital agency specializing in web development, design, and digital marketing. Our team of experts is dedicated to helping your business grow.',
})
print("✓ About Section created")

# Service Section
serviceSection.objects.get_or_create(id=1, defaults={
    'name': 'Web Development',
    'short_description': 'Professional web development services using modern technologies.',
    'fontawesome_icon_class': 'flaticon-growth',
})
serviceSection.objects.get_or_create(id=2, defaults={
    'name': 'UI/UX Design',
    'short_description': 'Beautiful and intuitive user interface designs.',
    'fontawesome_icon_class': 'flaticon-research',
})
serviceSection.objects.get_or_create(id=3, defaults={
    'name': 'Digital Marketing',
    'short_description': 'Grow your online presence with our marketing strategies.',
    'fontawesome_icon_class': 'flaticon-mission',
})
serviceSection.objects.get_or_create(id=4, defaults={
    'name': 'SEO Optimization',
    'short_description': 'Improve your search engine rankings and visibility.',
    'fontawesome_icon_class': 'flaticon-target',
})
print("✓ Service Section created")

# Fun Fact Section
funFactSection.objects.get_or_create(id=1, defaults={'fontawesome_icon_class': 'flaticon-happiness', 'title': 'Happy Clients', 'count': 1200, 'count_after': '+'})
funFactSection.objects.get_or_create(id=2, defaults={'fontawesome_icon_class': 'flaticon-project', 'title': 'Projects Done', 'count': 800, 'count_after': '+'})
funFactSection.objects.get_or_create(id=3, defaults={'fontawesome_icon_class': 'flaticon-customer-review', 'title': 'Great Reviews', 'count': 350, 'count_after': '+'})
funFactSection.objects.get_or_create(id=4, defaults={'fontawesome_icon_class': 'flaticon-trophy', 'title': 'Awards Won', 'count': 50, 'count_after': '+'})
print("✓ Fun Fact Section created")

# Project Category
cat1, _ = projectCategory.objects.get_or_create(id=1, defaults={'name': 'Web Design'})
cat2, _ = projectCategory.objects.get_or_create(id=2, defaults={'name': 'Development'})
cat3, _ = projectCategory.objects.get_or_create(id=3, defaults={'name': 'Marketing'})
print("✓ Project Categories created")

# Project Section
projectSection.objects.get_or_create(id=1, defaults={
    'title': 'E-Commerce Platform',
    'slug': 'e-commerce-platform',
    'category': cat1,
    'description': 'A modern e-commerce platform with advanced features.',
})
projectSection.objects.get_or_create(id=2, defaults={
    'title': 'Business Website',
    'slug': 'business-website',
    'category': cat2,
    'description': 'Professional business website with responsive design.',
})
projectSection.objects.get_or_create(id=3, defaults={
    'title': 'Marketing Campaign',
    'slug': 'marketing-campaign',
    'category': cat3,
    'description': 'Successful digital marketing campaign.',
})
print("✓ Projects created")

# Testimonial Section
testimonialsSection.objects.get_or_create(id=1, defaults={
    'name': 'John Smith',
    'position': 'CEO, TechCorp',
    'description': 'Excellent service and great results! The team was professional and delivered beyond our expectations.',
    'star': 5,
})
testimonialsSection.objects.get_or_create(id=2, defaults={
    'name': 'Jane Doe',
    'position': 'Marketing Director',
    'description': 'Professional team and amazing work! They transformed our online presence completely.',
    'star': 5,
})
testimonialsSection.objects.get_or_create(id=3, defaults={
    'name': 'Mike Johnson',
    'position': 'Business Owner',
    'description': 'Highly recommended! Their expertise helped us achieve our business goals.',
    'star': 5,
})
print("✓ Testimonials created")

# Client Section
clientSection.objects.get_or_create(id=1, defaults={'client_name': 'Client 1'})
clientSection.objects.get_or_create(id=2, defaults={'client_name': 'Client 2'})
clientSection.objects.get_or_create(id=3, defaults={'client_name': 'Client 3'})
clientSection.objects.get_or_create(id=4, defaults={'client_name': 'Client 4'})
print("✓ Client Section created")

# Blog Category
blog_cat1, _ = blogCategory.objects.get_or_create(id=1, defaults={'title': 'Business', 'slug': 'business'})
blog_cat2, _ = blogCategory.objects.get_or_create(id=2, defaults={'title': 'Technology', 'slug': 'technology'})
blog_cat3, _ = blogCategory.objects.get_or_create(id=3, defaults={'title': 'Design', 'slug': 'design'})
print("✓ Blog Categories created")

# Blogs
Blogs.objects.get_or_create(id=1, defaults={
    'title': 'How to Grow Your Business Online',
    'slug': 'how-to-grow-your-business-online',
    'author': 'Admin',
    'description': '<p>Learn the best strategies for growing your business in the digital age. This comprehensive guide covers everything from SEO to social media marketing.</p>',
    'category': blog_cat1,
})
Blogs.objects.get_or_create(id=2, defaults={
    'title': 'Latest Web Development Trends',
    'slug': 'latest-web-development-trends',
    'author': 'Admin',
    'description': '<p>Discover the latest trends in web development including new frameworks, technologies, and best practices for building modern websites.</p>',
    'category': blog_cat2,
})
Blogs.objects.get_or_create(id=3, defaults={
    'title': 'UI Design Best Practices',
    'slug': 'ui-design-best-practices',
    'author': 'Admin',
    'description': '<p>Master the art of UI design with these essential tips and best practices that will help you create beautiful user interfaces.</p>',
    'category': blog_cat3,
})
print("✓ Blogs created")

# Blog Page SEO
blogPageSEO.objects.get_or_create(id=1, defaults={
    'meta_title': 'Blog - TCG Agency',
    'meta_description': 'Read our latest blog posts about web development, design, and digital marketing.',
})
print("✓ Blog Page SEO created")

# Website Settings
websiteSetting.objects.get_or_create(id=1, defaults={
    'name': 'TCG Agency',
    'author': 'TCG Team',
    'email_address': 'info@tcgagency.com',
    'phone': '+1234567890',
    'address': '123 Main Street',
    'city': 'New York',
    'country': 'USA',
    'primary_color': '#75dab4',
    'secondary_color': '#1a1a1a',
})
print("✓ Website Settings created")

# Header Footer Setting
headerFooterSetting.objects.get_or_create(id=1, defaults={
    'footer_col1_description': 'We are a creative digital agency specializing in web development and design.',
    'footer_copyright': '© 2025 TCG Agency. All Rights Reserved.',
    'header_button_text': 'Contact Us',
    'header_button_url': '/contact',
    'social1_icon': 'fab fa-facebook-f',
    'social1_link': '#',
    'social2_icon': 'fab fa-twitter',
    'social2_link': '#',
    'social3_icon': 'fab fa-instagram',
    'social3_link': '#',
    'social4_icon': 'fab fa-linkedin-in',
    'social4_link': '#',
})
print("✓ Header Footer Settings created")

# SEO Setting
SeoSetting.objects.get_or_create(id=1, defaults={
    'meta_title': 'TCG Agency - Creative Digital Agency',
    'meta_description': 'Professional web development and digital marketing services.',
    'tag_line': 'Your Digital Success Partner',
})
print("✓ SEO Settings created")

# Pricing Section
pricingSection.objects.get_or_create(id=1, defaults={
    'title': 'Basic',
    'price': '29',
    'description': '5 Projects, 10GB Storage, Email Support, Basic Analytics',
    'button_text': 'Get Started',
    'button_url': '/contact',
})
pricingSection.objects.get_or_create(id=2, defaults={
    'title': 'Standard',
    'price': '59',
    'description': '15 Projects, 50GB Storage, Priority Support, Advanced Analytics',
    'is_featured': True,
    'button_text': 'Get Started',
    'button_url': '/contact',
})
pricingSection.objects.get_or_create(id=3, defaults={
    'title': 'Premium',
    'price': '99',
    'description': 'Unlimited Projects, 100GB Storage, 24/7 Support, Custom Analytics',
    'button_text': 'Get Started',
    'button_url': '/contact',
})
print("✓ Pricing Plans created")

# Pricing Page SEO
pricingPageSEO.objects.get_or_create(id=1, defaults={
    'meta_title': 'Pricing - TCG Agency',
    'meta_description': 'Check out our affordable pricing plans.',
})
print("✓ Pricing Page SEO created")

# Section Titles
serviceSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Our Services', 'title_big': 'What We Offer'})
projectSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Our Portfolio', 'title_big': 'Recent Projects'})
testimonialSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Testimonials', 'title_big': 'What Clients Say'})
blogSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Latest News', 'title_big': 'Our Blog'})
teamSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Our Team', 'title_big': 'Meet Our Experts'})
clientSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Our Clients', 'title_big': 'Trusted By'})
funfactSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Fun Facts', 'title_big': 'Our Achievements'})
pricingSectionTitle.objects.get_or_create(id=1, defaults={'title_small': 'Pricing', 'title_big': 'Our Packages'})
print("✓ Section Titles created")

# Contact Form Title
ContactFormTitle.objects.get_or_create(id=1, defaults={
    'contact_form_title': 'Have Any Questions',
    'name_field_placeholder': 'Enter your name',
    'email_field_placeholder': 'Enter your email',
    'phone_field_placeholder': 'Enter your phone',
    'subject_field_placeholder': 'Enter your subject',
    'message_field_placeholder': 'Enter your message',
    'submit_button_text': 'Send Message',
    'email_title': 'Email',
    'location_title': 'Location',
    'phone_title': 'Phone',
})
print("✓ Contact Form Title created")

# Contact Page SEO
contactPageSEO.objects.get_or_create(id=1, defaults={
    'meta_title': 'Contact Us - TCG Agency',
    'meta_description': 'Get in touch with us for your project inquiries.',
})
print("✓ Contact Page SEO created")

# Subscriber Form Title
SubscriberFormTitle.objects.get_or_create(id=1, defaults={
    'top_title': 'Get In Touch',
    'middle_title': 'Subscribe Our',
    'bottom_title': 'Newsletter',
    'email_field_placeholder': 'Enter your email',
    'submit_button_text': 'Subscribe',
})
print("✓ Subscriber Form Title created")

# Primary Menu
primaryMenu.objects.get_or_create(id=1, defaults={'name': 'Home', 'url': '/', 'order': 1})
primaryMenu.objects.get_or_create(id=2, defaults={'name': 'About', 'url': '/about', 'order': 2})
primaryMenu.objects.get_or_create(id=3, defaults={'name': 'Services', 'url': '/service', 'order': 3})
primaryMenu.objects.get_or_create(id=4, defaults={'name': 'Projects', 'url': '/projects', 'order': 4})
primaryMenu.objects.get_or_create(id=5, defaults={'name': 'Blog', 'url': '/blogs', 'order': 5})
primaryMenu.objects.get_or_create(id=6, defaults={'name': 'Pricing', 'url': '/pricing', 'order': 6})
primaryMenu.objects.get_or_create(id=7, defaults={'name': 'Contact', 'url': '/contact', 'order': 7})
print("✓ Primary Menu created")

# Home Page SEO
homePageSEO.objects.get_or_create(id=1, defaults={
    'meta_title': 'TCG Agency - Creative Digital Agency',
    'meta_description': 'Professional web development and digital marketing services. We help businesses grow online.',
})
print("✓ Home Page SEO created")

print("\n✅ All sample data loaded successfully!")
print("🌐 Visit http://127.0.0.1:8000 to see your website!")
