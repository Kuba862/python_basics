from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from .forms import MyForm
from .models import MyModel
from datetime import datetime

def home_view(request, year=datetime.now().strftime('%Y'), month=datetime.now().strftime('%B'), day=datetime.now().strftime("%d")):
    now = datetime.now()
    time = now.strftime('%H:%M')
    form = InputForm(request.POST or None)
    day = now.strftime('%d')
    return render(request,
        "app/home.html", {
        "year": year,
        "month": month,
        "day": day,
        "time": time,
        "form": InputForm(),
        "name": "Jakub",
        "lastName": "Rejch",
        "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore ipsa placeat atque nisi at debitis? Possimus, cupiditate id odit laborum repellendus ipsa quos? Magnam inventore a dolores reprehenderit nam molestiae?Nisi possimus iste non quisquam id quibusdam fuga aut enim tempora molestiae facere officiis, consequatur vero nesciunt ex sit ullam? Quia nam non corporis minima. Ducimus iure officia placeat deserunt!Laborum deleniti quam, officiis cum iusto reiciendis eum facere nihil nobis quis perferendis laboriosam, dolorum totam pariatur fuga eos nostrum omnis ullam optio libero. Unde officiis iste perferendis nulla commodi!Laudantium minus ad blanditiis exercitationem quaerat? Optio quis voluptatum laboriosam. Aperiam minima quaerat modi quo numquam facilis fuga laboriosam! Consectetur error aspernatur quia tenetur officiis dolorem amet, iure optio quidem!Temporibus modi distinctio est consectetur accusamus eius molestias quaerat sint laborum nam. Eaque voluptatibus at hic eos dolor accusantium veniam, id illo voluptatum qui dolores iure distinctio animi a. Doloremque.Obcaecati quibusdam nesciunt facilis debitis voluptatibus unde dicta vitae quam eaque! Dolor fuga, nisi aliquid ab assumenda at minima iure cumque quaerat eveniet illo voluptatem suscipit quibusdam quo? Rem, illo.Rem reiciendis blanditiis autem facilis distinctio sunt, odio quas deserunt necessitatibus consequatur quaerat eius quam consequuntur quos cumque ipsum cupiditate quis aliquid perspiciatis laboriosam iure. Excepturi nisi itaque quos quidem?Possimus, adipisci? Minima earum corporis mollitia ea atque molestias consequuntur quasi sed. Aliquam eaque suscipit enim fugit? Mollitia error voluptates cupiditate ipsam voluptatem rerum soluta, excepturi eaque sunt praesentium maiores!Maxime, natus ducimus quasi ea tenetur dignissimos quae earum asperiores praesentium unde harum ullam deserunt doloribus quis quo cumque. Qui aliquid aspernatur corporis molestias unde corrupti quaerat voluptatum laudantium optio.Vel inventore atque voluptates eligendi, officia cum odio. Sed, hic odio. Officiis, quidem perferendis in sit nemo ea doloribus necessitatibus quas veritatis illo ratione quam quae culpa nulla architecto natus! Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore ipsa placeat atque nisi at debitis? Possimus, cupiditate id odit laborum repellendus ipsa quos? Magnam inventore a dolores reprehenderit nam molestiae? Nisi possimus iste non quisquam id quibusdam fuga aut enim tempora molestiae facere officiis, consequatur vero nesciunt ex sit ullam? Quia nam non corporis minima. Ducimus iure officia placeat deserunt! Laborum deleniti quam, officiis cum iusto reiciendis eum facere nihil nobis quis perferendis laboriosam, dolorum totam pariatur fuga eos nostrum omnis ullam optio libero. Unde officiis iste perferendis nulla commodi! Laudantium minus ad blanditiis exercitationem quaerat? Optio quis voluptatum laboriosam. Aperiam minima quaerat modi quo numquam facilis fuga laboriosam! Consectetur error aspernatur quia tenetur officiis dolorem amet, iure optio quidem! Temporibus modi distinctio est consectetur accusamus eius molestias quaerat sint laborum nam. Eaque voluptatibus at hic eos dolor accusantium veniam, id illo voluptatum qui dolores iure distinctio animi a. Doloremque. Obcaecati quibusdam nesciunt facilis debitis voluptatibus unde dicta vitae quam eaque! Dolor fuga, nisi aliquid ab assumenda at minima iure cumque quaerat eveniet illo voluptatem suscipit quibusdam quo? Rem, illo. Rem reiciendis blanditiis autem facilis distinctio sunt, odio quas deserunt necessitatibus consequatur quaerat eius quam consequuntur quos cumque ipsum cupiditate quis aliquid perspiciatis laboriosam iure. Excepturi nisi itaque quos quidem? Possimus, adipisci? Minima earum corporis mollitia ea atque molestias consequuntur quasi sed. Aliquam eaque suscipit enim fugit? Mollitia error voluptates cupiditate ipsam voluptatem rerum soluta, excepturi eaque sunt praesentium maiores! Maxime, natus ducimus quasi ea tenetur dignissimos quae earum asperiores praesentium unde harum ullam deserunt doloribus quis quo cumque. Qui aliquid aspernatur corporis molestias unde corrupti quaerat voluptatum laudantium optio. Vel inventore atque voluptates eligendi, officia cum odio. Sed, hic odio. Officiis, quidem perferendis in sit nemo ea doloribus necessitatibus quas veritatis illo ratione quam quae culpa nulla architecto natus!",
                          })

def title_view(request):
    context = {}
    context["dataset"] = MyModel.objects.all()
    return render(request, "title_view.html", context)

def about_view(request):
    return render(request,
        "app/about.html", {
        "text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure, commodi aliquid earum cumque alias doloribus animi odit, obcaecati mollitia repellat facilis ipsam ea deleniti, quia perferendis iste atque incidunt eveniet. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure, commodi aliquid earum cumque alias doloribus animi odit, obcaecati mollitia repellat facilis ipsam ea deleniti, quia perferendis iste atque incidunt eveniet. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure, commodi aliquid earum cumque alias doloribus animi odit, obcaecati mollitia repellat facilis ipsam ea deleniti, quia perferendis iste atque incidunt eveniet. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure, commodi aliquid earum cumque alias doloribus animi odit, obcaecati mollitia repellat facilis ipsam ea deleniti, quia perferendis iste atque incidunt eveniet. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure, commodi aliquid earum cumque alias doloribus animi odit, obcaecati mollitia repellat facilis ipsam ea deleniti. Lorem",
                  })

def create_view(request):
    context = {}
    form = MyForm(request.POST or None)
    if form.iv_valid():
        form.save()
    context['dataset'] = MyModel.objects.all()
    return render(request, "createView.html", context)