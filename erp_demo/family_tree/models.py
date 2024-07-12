from django.db import models


class FamilyTree(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)

    family_tree = models.ForeignKey(FamilyTree, on_delete=models.CASCADE)
    father = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
    )
    mother = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
    )
    siblings = models.ManyToManyField(
        'self',
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_children(self):
        return self.children.all()

    def get_siblings(self):
        return self.siblings.all()

    def get_parents(self):
        return [self.father, self.mother]
    
    def get_grandparents(self):
        return [parent for parent in self.get_parents() if parent]

    def get_grandchildren(self):
        return [child for child in self.get_children() if child]
