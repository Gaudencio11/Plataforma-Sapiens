from django.urls import path, re_path
from .views import  menuView, daysView, roomsGenericView, padletView, desopilarView, programacaoView, get_excell_users, apoiadoresView, loginRedirect
from allauth.account  import views

#Have to configure to all paths use the slug

urlpatterns = [
    # Accounts Urls
    path('', views.login, name='account_login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='account_signup'),

    #esse serve para abrir a página dizendo que seu email de verificação foi enviado (o mais simples)
    path(
        "email/email-enviado/",
        views.email_verification_sent,
        name="account_email_verification_sent",
    ),
    #esse serve para realizar o envio do email de confirmação para o usuário
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        views.confirm_email,
        name="account_confirm_email",
    ),
    #Reset password
    path("redefinir-senha/", views.password_reset, name="account_reset_password"
    ),
    path(
        "senha/email-enviado/",
        views.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.password_reset_from_key,
        name="account_reset_password_from_key",),
    path(
        "password/reset/key/done/",
        views.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),


    #site urls
    path('hall/', menuView, name = 'menu'),
    path('<slug:slug1>/padlet', padletView, name='padlet'),
    path('<slug:slug1>/desopilar', desopilarView, name='desopilar'),
    path('<slug:slug1>/programacao', programacaoView, name = 'programacao'),
    path('<slug:slug1>/apoiadores', apoiadoresView, name = 'apoiadores'),
    path('<slug:slug1>/<slug:slug2>/dias', daysView, name='days'),
    path('<slug:slug1>/<slug:slug2>/dia-<slug:slug3>/', roomsGenericView, name = 'rooms'),
    path('excell_users/', get_excell_users, name = "get_excell_users"),
    path('bem-vindo/', loginRedirect, name='bem_vindo')
    #Testes
    
]


"""   
    
    
    #Reset password
    path("redefinir-senha/", views.password_reset, name="account_reset_password"
    ),
    path(
        "password/reset/done/",
        views.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.password_reset_from_key,
        name="account_reset_password_from_key",),
    path(
        "password/reset/key/done/",
        views.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
    """