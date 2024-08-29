import json
from aiogram import types
from django.http import JsonResponse, HttpResponseNotFound
from django.views import View

from bot.app import dp
from bot.models import TgUser


class BotView(View):
    async def post(self, request, *args, **kwargs):
        update = json.loads(request.body.decode('utf-8'))
        await dp.process_update(types.Update(**update))
        return JsonResponse({"status": "ok"})

    async def get(self, request, *args, **kwargs):
        return HttpResponseNotFound("Not found")


class SendMessagesView(View):

    async def send(self, message, chat_id):
        try:
            await dp.bot.send_message(chat_id, message)
        except Exception as e:
            print(e)

    async def post(self, request, *args, **kwargs):
        update = json.loads(request.body.decode('utf-8'))
        message = update.get('message')
        if not message:
            return JsonResponse({"status": "fail", "message": "Message not found"})
        users = [user async for user in TgUser.objects.all()]
        for user in users:
            await self.send(message, user.user_id)
        return JsonResponse({"status": "ok"})
