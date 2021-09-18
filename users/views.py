from django.shortcuts import render
from .models import Profile

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    user = Profile.objects.get(id=pk)
    topSkills = user.skill_set.exclude(description__exact="")
    otherSkills = user.skill_set.filter(description="")
    context =  {'user':user, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/profile.html', context)
