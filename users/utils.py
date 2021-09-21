from django.db.models import Q
from .models import Profile, Skill

def searchProfiles(request): 
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')

    skills = Skill.objects.filter(name__icontains=search)

    # filter -> or  === Q(...) | Q(...)
    #           and === Q(...) & Q(...)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search) | 
        Q(headline__icontains=search) | 
        Q(skill__in=skills)
        )

    return profiles, search