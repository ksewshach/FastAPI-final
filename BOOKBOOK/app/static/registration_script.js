   
        
        


        // Добавляем обработчик события для формы
        const form = document.querySelector('form');
        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Предотвращаем стандартное поведение отправки формы

            // Проверка введенных данных (рекомендуется сделать на сервере)
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const passwordConfirm = document.getElementById('password-confirm').value;

            // Валидация введенных данных
            let isValid = true;

            // Проверка имени пользователя (можно добавить более строгую валидацию)
            if (username.trim() === "") {
                document.getElementById('username-error').textContent = "Пожалуйста, введите имя пользователя.";
                isValid = false;
            } else {
                document.getElementById('username-error').textContent = "";
            }

            // Проверка email (можно добавить более строгую валидацию)
            if (email.trim() === "" || !email.includes("@")) {
                document.getElementById('email-error').textContent = "Пожалуйста, введите корректный email.";
                isValid = false;
            } else {
                document.getElementById('email-error').textContent = "";
            }

            // Проверка пароля
            if (password.trim() === "" || password.length < 8) {
                document.getElementById('password-error').textContent = "Пароль должен быть не менее 8 символов.";
                isValid = false;
            } else {
                document.getElementById('password-error').textContent = "";
            }

            // Проверка подтверждения пароля
            if (passwordConfirm.trim() === "" || passwordConfirm !== password) {
                document.getElementById('password-confirm-error').textContent = "Пароли не совпадают.";
                isValid = false;
            } else {
                document.getElementById('password-confirm-error').textContent = "";
            }

            // Если форма прошла проверку, отправляем данные на сервер
            if (isValid) {
                // Отправка данных на сервер (замените это на реальную отправку)
                console.log("Форма отправлена");
            }
        });