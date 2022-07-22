from django.shortcuts import render

petitions = [
    {
        'id': 1,
        'title': 'title of the petition 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus dolores, dicta temporibus delectus aspernatur eaque dolor accusantium eos ipsam inventore consequatur dolore voluptatibus ipsum recusandae! Aspernatur deserunt odit ipsam praesentium. Tempore obcaecati deserunt, rerum quasi asperiores sunt. Odit sit delectus voluptatibus, eum iure itaque dignissimos? Quo nam saepe nemo voluptatibus placeat, voluptate esse at provident quisquam blanditiis a sapiente labore.',
    },
    {
        'id': 2,
        'title': 'title of the petition 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus dolores, dicta temporibus delectus aspernatur eaque dolor accusantium eos ipsam inventore consequatur dolore voluptatibus ipsum recusandae! Aspernatur deserunt odit ipsam praesentium. Tempore obcaecati deserunt, rerum quasi asperiores sunt. Odit sit delectus voluptatibus, eum iure itaque dignissimos? Quo nam saepe nemo voluptatibus placeat, voluptate esse at provident quisquam blanditiis a sapiente labore.',
    },
    {
        'id': 3,
        'title': 'title of the petition 3',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus dolores, dicta temporibus delectus aspernatur eaque dolor accusantium eos ipsam inventore consequatur dolore voluptatibus ipsum recusandae! Aspernatur deserunt odit ipsam praesentium. Tempore obcaecati deserunt, rerum quasi asperiores sunt. Odit sit delectus voluptatibus, eum iure itaque dignissimos? Quo nam saepe nemo voluptatibus placeat, voluptate esse at provident quisquam blanditiis a sapiente labore.',
    }
]

def homePage(request):
    context = {
        'petitions': petitions,
    }
    return render(request, 'citizengo/homePage.html', context)

def petitionPage(request, id):
    petition = None
    for i in petitions:
        if i['id'] == int(id):
            petition = i
    context = {"petition": petition}
    return render(request, 'citizengo/petitionPage.html', context)

def aboutUsPage(request):
    return render(request, 'citizengo/aboutUs.html')

def victoriesPage(request):
    return render(request, 'citizengo/victories.html')    

