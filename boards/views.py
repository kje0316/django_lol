from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import (
    User,
    Champions,
    Review,
    champion_skill_img_text,
    champion_tip,
    Champion_counter,
    Champion_rate,
    champion_skill_name,
    Champion_story,
)
from django.contrib.auth.models import User
from .forms import ReviewForm


def index(request):
    board_list = champion_tip.objects.all()
    return render(request, "boards/index.html", {"board_list": board_list})


def board_detail(request, champion_id):
    # 요청하는 요소: db에서 가져오고자 하는 컬럼의 값 ex) champion 테이블의 champion값
    ChampionBoard = (
        Champions.objects.filter()
        .prefetch_related("review_set")
        .get(champion=champion_id)
    )
    # ChampionBoard = 테이블에서 가져온 값들을 저장할 변수, orm으로 가져오고자 할 때 ex) champion은 가져오고자 하는 값
    ChampionTipBoard = champion_tip.objects.filter().get(champion=champion_id)
    ChampionSkillImgBoard = champion_skill_img_text.objects.filter().get(
        champion=champion_id
    )
    ChampionCounterBoard = Champion_counter.objects.filter(champion=champion_id).all()
    ChampionRateBoard = Champion_rate.objects.filter().get(champion=champion_id)
    ChampionSkillNameBoard = champion_skill_name.objects.filter().get(
        champion=champion_id
    )
    ChampionStoryBoard = Champion_story.objects.filter().get(champion=champion_id)

    # 댓글 board
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Review(content=data["review"], ChampionBoard=ChampionBoard)
            review.save()
            return redirect(
                reverse("ChampionBoard:detail", kwargs={"champion_id": champion_id})
            )

    return render(
        request,
        "boards/detail.html",
        {
            "ChampionBoard": ChampionBoard,
            "ChampionTipBoard": ChampionTipBoard,
            "ChampionSkillImgBoard": ChampionSkillImgBoard,
            "ChampionCounterBoard": ChampionCounterBoard,
            "ChampionRateBoard": ChampionRateBoard,
            "ChampionSkillNameBoard": ChampionSkillNameBoard,
            "ChampionStoryBoard": ChampionStoryBoard,
            "form": form,
        },
    )