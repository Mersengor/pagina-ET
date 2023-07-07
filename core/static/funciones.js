function showRegistro(sw){
    var login = document.querySelector("#login");
    var regis = document.querySelector("#registro");
    login.classList.add(sw?"hide":"showLogin");
    regis.classList.add(sw?"show":"hide");
    login.classList.remove(!sw?"hide":"showLogin");
    regis.classList.remove(!sw?"show":"hide");
    return false;
}
