import React from 'react'

const Footer = () => {
    return (
        <div class="container-lg mt-auto">
            <div class="row justify-content-center">
                <div class="col-sm-6 col-md-3 text-center">
                    <p>
                        <strong>My TODO</strong>
                    </p>
                    <p>
                        <ul class="list-unstyled">
                            <li><a href="{% url 'mainapp:main_page' %}">Домашняя</a></li>
                            <li><a href="{% url 'authapp:logout' %}">Выйти или Войти</a></li>
                        </ul>
                    </p>
                </div>
                <div class="col-sm-6 col-md-3 text-center">
                    <p>
                        <strong>Полезное</strong>
                    </p>
                    <p>
                        <ul class="list-unstyled">
                            <li><a href="#">Положения &amp; Условия</a></li>
                            <li><a href="#">Конфиденциальность &amp; Cookies</a></li>
                            <li><a href="#">Документация по API</a></li>
                            <li><a href="#">Документация по сайту</a></li>
                        </ul>
                    </p>
                </div>
                <div class="col-sm-6 col-md-3 text-center">
                    <p>
                        <strong>Мы в социальных сетях</strong>
                    </p>
                    <p>
                        <div class="row justify-content-around">
                            <div><a href="#"><i class="fab fa-vk fa-2x"></i></a></div>
                            <div><a href="#"><i class="fab fa-facebook-f fa-2x"></i></a></div>
                            <div><a href="#"><i class="fab fa-instagram fa-2x"></i></a></div>
                            <div><a href="#"><i class="fab fa-pinterest-p fa-2x"></i></a></div>
                        </div>
                    </p>
                    <p>
                        <strong>Наше приложение</strong>
                    </p>
                    <p>
                        <div class="row justify-content-around">
                            <div><a href="#"><i class="fab fa-app-store fa-2x"></i></a></div>
                            <div><a href="#"><i class="fab fa-google-play fa-2x"></i></a></div>
                            <div><a href="#"><i class="fab fa-windows fa-2x"></i></a></div>
                        </div>
                    </p>
                </div>
            </div>
            <div class="row justify-content-center">
                <div>
                    <p><small>&copy; My TODO 2023</small></p>
                </div>
            </div>
        </div>
)
}
export default Footer
