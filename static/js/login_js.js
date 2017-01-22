window.onload = function(){
    mStatus();
}

var VaildName = document.getElementById('VaildName');
var VaildPsw = document.getElementById('VaildPsw');

function validate_required(field, alerttxt)
{
    with (field)
    {
        if (value == null || value == "")
        {
            if (field == inputName)
                VaildName.innerText = alerttxt;
            if (field == inputPsw)
                VaildPsw.innerText = alerttxt;
            return false;
        }
        else
        {
            return true;
        }
    }
}

function validate_form(thisform)
{
    with (thisform)
    {
        if (validate_required(inputName,"*名字不能为空！") == false)
        {
            inputName.focus();
            return false;
        }
        if (validate_required(inputPsw,"*密码不能为空！") == false)
        {
            inputPsw.focus();
            return false;
        }
    }
}


function mStatus() {
    var mbtn = document.getElementById('m_id');
    if(mbtn.name == 'logn')
    {
        mbtn.style.display = 'none';
    }
}