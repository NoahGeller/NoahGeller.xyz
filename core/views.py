from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def robots(request):
    lines = [
        'Sitemap: https://noahgeller.xyz/sitemap.xml',
        'User-Agent: *',
        'Disallow: /admin/',
        'Allow: /',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')

def sitemap(request):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '<url>',
        '<loc>https://noahgeller.xyz/</loc>',
        '</url>',
        '<url>',
        '<loc>https://noahgeller.xyz/blog</loc>',
        '</url>',
        '<url>',
        '<loc>https://noahgeller.xyz/portfolio/</loc>',
        '</url>',
        '<url>',
        '<loc>https://noahgeller.xyz/about</loc>',
        '</url>',
        '</urlset>',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/xml')

def error_404(request, exception):
    return render(request, 'core/error_404.html')

def error_500(request):
    return render(request, 'core/error_500.html')
