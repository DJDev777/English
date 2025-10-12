# from django.db import models

# class EnglishLevel(models.Model):
#     name = models.CharField(verbose_name='Cefr Level sufix', max_length=3)
#     description = models.CharField(verbose_name='Cefr Level text', max_length=50)

#     class Meta:
#         ordering = ('name',)

#     def __str__(self):
#         return f'{self.name} - {self.description}'


# class CefrWordsList(models.Model):
#     cefr_level = models.ForeignKey(EnglishLevel, on_delete=models.CASCADE, related_name="cefr_lists")
#     word = models.ManyToManyField("Word", related_name="cefr_lists")
#     translate_ka = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=200, blank=True, null=True)
#     info = models.TextField(blank=True, null=True)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)

#     class Meta:
#         verbose_name = "CEFR Words List"
#         verbose_name_plural = "CEFR Words Lists"
#         ordering = ["cefr_level__name"]

#     def __str__(self):
#         return f"CEFR {self.cefr_level} Words"
    