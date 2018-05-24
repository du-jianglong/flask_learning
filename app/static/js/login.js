function set_openid(openid, name) {
    var u = openid.search('<username>');
    if (u != -1) {
        // openid 需要 username
        var user = prompt('Enter your ' + openid + ' username: ');
        openid = openid.substr(0, u) + user;
    }

    var form = document.forms['login'];
    form.elements['openid'].value = openid;
}