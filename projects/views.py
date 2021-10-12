from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects


def projects(request):
    projects, search = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 3)
    
    context = {'projects': projects, 'search':search, 'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()

        project.getVoteCount

        messages.success(request, 'Message sent successfully')

        return redirect('project', pk=project.id)

    return render(request, 'projects/project.html', {'project': project, 'form':form})


@login_required(login_url="login")
def createProject(request):
    page = 'create'
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # link project owner to profile !!!
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form': form, 'page':page}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    page = 'update'
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form, 'page':page}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object':project}
    return render(request, 'delete_template.html', context)

