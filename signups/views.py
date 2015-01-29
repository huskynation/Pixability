from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect
from django import forms
from .forms import UploadFileForm

# Create your views here.


from .forms import SignUpForm


def home(request):



    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def thankyou(request):
    form = SignUpForm(request.POST or None  )

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, "We'll be in touch")
        return HttpResponseRedirect('/thank-you/')

    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))
def team(request):
    return render_to_response("team.html",
                              locals(),
                              context_instance=RequestContext(request))

def ourstory(request):
    return render_to_response("ourstory.html",
                              locals(),
                              context_instance=RequestContext(request))
def blog(request):
    return render_to_response("blog.html",
                              locals(),
                              context_instance=RequestContext(request))
def borrower(request):
    return render_to_response("borrower.html",
                              locals(),
                              context_instance=RequestContext(request))
def lender(request):
    return render_to_response("lender.html",
                              locals(),
                              context_instance=RequestContext(request))
def process(request):
    return render_to_response("process.html",
                              locals(),
                              context_instance=RequestContext(request))
def careers(request):
    return render_to_response("careers.html",
                              locals(),
                              context_instance=RequestContext(request))
def upload(request):
    return render_to_response("upload.html",
                              locals(),
                              context_instance=RequestContext(request))
#def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['uploadedfile'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

# class PDFUploadView(CreateView):
#   model = PDFUpload
#   form_class = UploadFileForm
#   template_name = 'upload.html'
#   success_url = '/thanks/'
