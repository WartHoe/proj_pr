from locust import HttpUser, task, between
import random

class PollUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def load_questions(self):
        with self.client.get("/api/questions/", catch_response=True) as response:
            if response.ok:
                questions = response.json()
                if questions and isinstance(questions, list):
                    question = random.choice(questions)
                    self.client.get(f"/api/questions/{question['id']}/")
    
    @task(1)
    def vote(self):
        # Получаем вопросы
        with self.client.get("/api/questions/", catch_response=True) as response:
            if not response.ok:
                return
            
            questions = response.json()
            if not questions or not isinstance(questions, list):
                return
            
            # Выбираем случайный вопрос
            question = random.choice(questions)
            
            # Получаем варианты ответа
            with self.client.get(f"/api/questions/{question['id']}/", catch_response=True) as choices_response:
                if not choices_response.ok:
                    return
                
                choices = choices_response.json()
                if not choices or not isinstance(choices, list):
                    return
                
                # Выбираем случайный вариант и голосуем
                choice = random.choice(choices)
                self.client.post(
                    f"/api/choices/{choice['id']}/vote/",
                    headers={"Content-Type": "application/json"},
                    catch_response=True
                )