from playwright.sync_api import sync_playwright
import random
import time

def test_poll_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(10000)  # Увеличиваем таймаут
        
        try:
            # Переходим на страницу
            page.goto("https://glowing-tribble-4v6xrw5vx5xcpjq-5500.app.github.dev")
            
            # Проверяем, не попали ли на страницу Codespaces Access Port
            if "Codespaces Access Port" in page.title():
                print("Обнаружена страница Codespaces Access Port, нажимаем Continue...")
                page.click("button:has-text('Continue')")
                page.wait_for_load_state("networkidle")  # Ждем загрузки после нажатия
                time.sleep(2)  # Небольшая задержка для надежности
            
            # Повторно проверяем заголовок
            actual_title = page.title()
            print(f"Фактический заголовок после проверки: '{actual_title}'")
            
            if "опросник" not in actual_title.lower():
                raise AssertionError(f"После обхода защиты не найден заголовок 'Опросник', получено: '{actual_title}'")
            
            # Остальная часть теста (как в предыдущем коде)
            page.wait_for_selector(".question")
            questions = page.locator(".question").all()
            print(f"Найдено {len(questions)} вопросов")
            
            for question in questions:
                question_text = question.locator("h3").text_content()
                print(f"\nОбрабатываем вопрос: {question_text}")
                
                choices = question.locator(".choices input[type='radio']").all()
                if choices:
                    random_choice = random.choice(choices)
                    random_choice.click()
            
            with page.expect_event("dialog") as dialog_info:
                page.locator("button[type='submit']").click()
            
            dialog = dialog_info.value
            dialog.accept()
            print("\nТест успешно завершен!")
                
        except Exception as e:
            print(f"\nОшибка: {str(e)}")
            page.screenshot(path="test_failure.png")
            print("Скриншот сохранен как test_failure.png")
            raise
        finally:
            browser.close()

if __name__ == "__main__":
    test_poll_form()