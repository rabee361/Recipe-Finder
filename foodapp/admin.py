from django.contrib import admin
from .models import *
from .resources import IngredientsRes
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()



def export_to_pdf_reportlab(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recipes.pdf"'
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Key-value pairs
    for recipe in queryset:
        elements.append(Paragraph(f"Name: {recipe.name}", styles['Normal']))
        elements.append(Paragraph(f"Description: {recipe.description}", styles['Normal']))
        elements.append(Spacer(1, 12))

        # Table data
        data = [
            ['cuisine', 'time_to_cook'],  # Table header
            # Add table rows here for each ingredient in the recipe
        ]
        for recipe in Recipe.objects.all():
            data.append([
                recipe.cuisine,  # Replace with the actual field name for the ingredient name
                recipe.time_to_cook,  # Replace with the actual field name for the ingredient quantity
            ])

        # Create the table with the data
        table = Table(data, colWidths=[doc.width/3.0]*3)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        elements.append(table)
        elements.append(PageBreak())  # Add a page break after each recipe

    # Build the PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

   
# def export_to_pdf_reportlab(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recipes.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Start writing the PDF here
    y = height - 100  # Start Y position for the first line
    for recipe in queryset:
        p.drawString(100, y, f"Name: {recipe.name}")
        y -= 20  # Move Y position for next line
        p.drawString(100, y, f"Description: {recipe.description}")
        y -= 40  # Move Y position for next line, add more space between recipes

        if y < 100:  # If we are close to the bottom of the page
            p.showPage()  # Finish the current page and start a new page
            y = height - 100  # Reset Y position for the new page

    p.showPage()
    p.save()
    return response
export_to_pdf_reportlab.short_description = "Export selected objects to PDF"

















@admin.register(Recipe)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    actions = [export_to_pdf_reportlab]

# admin.site.register(Recipe)
admin.site.register(Unit)
admin.site.register(Ingredient_name)
admin.site.register(Ingredient)
admin.site.register(Messages)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Cuisine)
admin.site.register(GalleryImage)