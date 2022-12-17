# qa_guru_python_3_7

Этот тест представлен в трех вариантах:
1. Чистый Selene (без шагов) (см.test/test_selene.py)
2. Лямбда шаги через with allure.step (см.test/test_steps.py)
3. Шаги с декоратором @allure.step (см.test/test_steps.py)
4. Разметку тестов всеми аннотациями (см. test/test_allure_annotations.py)

Run tests: 
- pytest tests/

Run allure reports:
- allure serve tests/allure_results
 