function attach_event_action_turn_left()
{//fonction qui fait tourner NAO a gauche
    $('.nao-move-turn-left').each(function()
    {//on regarde si on trouve l'élément avec la class nao-move-turn-left'
        $('.nao-move-turn-left').on('mousedown', function()
        {//quand on presse le bouton
            $('.nao-move-turn-left').attr('data-active', true);//on met l\'attribut data-active à true
            $.ajax(
                    {
                        type: "POST",
                        url: "../ajax/action",
                        dataType: "JSON",
                        data: {
                            'type_action': $('.nao-move-turn-left').attr('data-action'), //on récupère l\'attibut data-action
                            'data-active': $('.nao-move-turn-left').attr('data-active'), //on récupère l\'attibut data-active
                            'event': 'press'
                        },
                        success: function(data_result)
                        {//si succès
                            if ($('.nao-move-turn-left').attr('data-active'))
                            {//on regarde si data-active est à true
                                //TODO: Afficher le statut de nao qui marche
                                var texte = 'nao tourne a gauche';
                                $('.marche').text(texte);
                                //data_result['statut-execution']
                            }
                        }
                    });
        });

        $('.nao-move-turn-left').on('mouseup', function()
        {//quand on relâche le bouton
            if ($('.nao-move-turn-left').attr('data-active'))
            {//on regarde si data-active est à true
                $.ajax({
                    type: "POST",
                    url: "../ajax/action",
                    dataType: "JSON",
                    data: {
                        'type_action': $('.nao-move-turn-left').attr('data-action'),
                        'data-active': $('.nao-move-turn-left').attr('data-active'),
                        'event': 'unpress'
                    },
                    success: function(data_result)
                    {//si succès
                        //TODO: Arreter de marcher
                        var texte = ' nao ne tourne plus à gauche';
                        $('.marcheplus').text(texte);
                    }
                });
                $('.nao-move-turn-left').attr('data-active', false);//on passe data-active à false
            }
        });
    });
}

function attach_event_action_turn_right()
{//fonction qui fait avancer NAO
    $('.nao-move-turn-right').each(function()
    {//on regarde si on trouve l'élément avec la class nao-move-up
        $('.nao-move-turn-right').on('mousedown', function()
        {//quand on presse le bouton
            $('.nao-move-up').attr('data-active', true);//on met l\'attribut data-active à true
            $.ajax(
                    {
                        type: "POST",
                        url: "../ajax/action",
                        dataType: "JSON",
                        data: {
                            'type_action': $('.nao-move-turn-right').attr('data-action'), //on récupère l\'attibut data-action
                            'data-active': $('.nao-move-turn-right').attr('data-active'), //on récupère l\'attibut data-active
                            'event': 'press'
                        },
                        success: function(data_result)
                        {//si succès
                            if ($('.nao-move-turn-right').attr('data-active'))
                            {//on regarde si data-active est à true
                                //TODO: Afficher le statut de nao qui marche
                                var texte = 'nao tourne a droite';
                                $('.marche').text(texte);//data_result['statut-execution']
                            }
                        }
                    });
        });

        $('.nao-move-turn-right').on('mouseup', function()
        {//quand on relâche le bouton
            if ($('.nao-move-turn-right').attr('data-active'))
            {//on regarde si data-active est à true
                $.ajax({
                    type: "POST",
                    url: "../ajax/action",
                    dataType: "JSON",
                    data: {
                        'type_action': $('.nao-move-turn-right').attr('data-action'),
                        'data-active': $('.nao-move-turn-right').attr('data-active'),
                        'event': 'unpress'
                    },
                    success: function(data_result)
                    {//si succès
                        //TODO: Arreter de marcher
                        var texte = ' nao ne tourne plus à droite';
                        $('.marcheplus').text(texte);
                    }
                });
                $('.nao-move-turn-right').attr('data-active', false);//on passe data-active à false
            }
        });
    });
}

function attach_event_action_up()
{//fonction qui fait avancer NAO
    $('.nao-move-up').each(function()
    {//on regarde si on trouve l'élément avec la class nao-move-up
        $('.nao-move-up').on('mousedown', function()
        {//quand on presse le bouton
            $('.nao-move-up').attr('data-active', true);//on met l\'attribut data-active à true
            $.ajax(
                    {
                        type: "POST",
                        url: "../ajax/action",
                        dataType: "JSON",
                        data: {
                            'type_action': $('.nao-move-up').attr('data-action'), //on récupère l\'attibut data-action
                            'data-active': $('.nao-move-up').attr('data-active'), //on récupère l\'attibut data-active
                            'event': 'press'
                        },
                        success: function(data_result)
                        {//si succès
                            if ($('.nao-move-up').attr('data-active'))
                            {//on regarde si data-active est à true
                                //TODO: Afficher le statut de nao qui marche
                                var texte = 'nao marche';
                                $('.marche').text(texte);//data_result['statut-execution']
                            }
                        }
                    });
        });

        $('.nao-move-up').on('mouseup', function()
        {//quand on relâche le bouton
            if ($('.nao-move-up').attr('data-active'))
            {//on regarde si data-active est à true
                $.ajax({
                    type: "POST",
                    url: "../ajax/action",
                    dataType: "JSON",
                    data: {
                        'type_action': $('.nao-move-up').attr('data-action'),
                        'data-active': $('.nao-move-up').attr('data-active'),
                        'event': 'unpress'
                    },
                    success: function(data_result)
                    {//si succès
                        //TODO: Arreter de marcher
                        var texte = ' nao ne marche plus';
                        $('.marcheplus').text(texte);
                    }
                });
                $('.nao-move-up').attr('data-active', false);//on passe data-active à false
            }
        });
    });
}

function attach_event_action_right()
{//fonction qui fait tourner Nao à droite, même principe que attach_event_action_up()
    $('.nao-move-right').each(function()
    {
        $('.nao-move-right').on('mousedown', function()
        {
            $('.nao-move-right').attr('data-active', true);
            $.ajax(
                    {
                        type: "POST",
                        url: "../ajax/action",
                        dataType: "JSON",
                        data: {
                            'type_action': $('.nao-move-right').attr('data-action'),
                            'data-active': $('.nao-move-right').attr('data-active'),
                            'event': 'press'
                        },
                        success: function(data_result)
                        {
                            if ($('.nao-move-right').attr('data-active'))
                            {
                                //TODO: Afficher le statut de nao qui tourne à droite
                                var texte = 'nao tourne à droite';
                                $('.marche').text(texte);
                            }
                        }
                    });
        });

        $('.nao-move-right').on('mouseup', function()
        {
            if ($('.nao-move-right').attr('data-active'))
            {
                $.ajax({
                    type: "POST",
                    url: "../ajax/action",
                    dataType: "JSON",
                    data: {
                        'type_action': $('.nao-move-right').attr('data-action'),
                        'data-active': $('.nao-move-right').attr('data-active'),
                        'event': 'unpress'
                    },
                    success: function(data_result)
                    {
                        //TODO: Arreter de tourner à droite
                        var texte = ' nao ne tourne plus à droite';
                        $('.marcheplus').text(texte);
                    }
                });
                $('.nao-move-right').attr('data-active', false);
            }
        });
    });
}

function attach_event_action_down()
{//fonction qui fait reculer Nao, même principe que attach_event_action_up()
    $('.nao-move-down').each(function()
    {
        $('.nao-move-down').on('mousedown', function()
        {
            $('.nao-move-down').attr('data-active', true);
            $.ajax(
                    {
                        type: "POST",
                        url: "../ajax/action",
                        dataType: "JSON",
                        data: {
                            'type_action': $('.nao-move-down').attr('data-action'),
                            'data-active': $('.nao-move-down').attr('data-active'),
                            'event': 'press'
                        },
                        success: function(data_result)
                        {
                            if ($('.nao-move-down').attr('data-active'))
                            {
                                //TODO: Afficher le statut de nao qui recule
                                var texte = 'nao recule';
                                $('.marche').text(texte);
                            }
                        }
                    });
        });

        $('.nao-move-down').on('mouseup', function()
        {
            if ($('.nao-move-down').attr('data-active'))
            {
                $.ajax({
                    type: "POST",
                    url: "../ajax/action",
                    dataType: "JSON",
                    data: {
                        'type_action': $('.nao-move-down').attr('data-action'),
                        'data-active': $('.nao-move-down').attr('data-active'),
                        'event': 'unpress'
                    },
                    success: function(data_result)
                    {
                        //TODO: Arreter de reculer
                        var texte = ' nao ne recule plus';
                        $('.marcheplus').text(texte);
                    }
                });
                $('.nao-move-down').attr('data-active', false);
            }
        });
    });
}

function attach_event_action_left()
{//fonction qui fait tourner Nao à gauche, même principe que attach_event_action_up()
    $('.nao-move-left').each(function()
    {
        $('.nao-move-left').on('mousedown', function()
        {
            $('.nao-move-down').attr('data-active', true);
            $.ajax(
                    {
                        type: "POST",
                        url: "../ajax/action",
                        dataType: "JSON",
                        data: {
                            'type_action': $('.nao-move-left').attr('data-action'),
                            'data-active': $('.nao-move-left').attr('data-active'),
                            'event': 'press'
                        },
                        success: function(data_result)
                        {
                            if ($('.nao-move-left').attr('data-active'))
                            {
                                //TODO: Afficher le statut de nao qui tourne à gauche
                                var texte = 'nao tourne à gauche';
                                $('.marche').text(texte);
                            }
                        }
                    });
        });

        $('.nao-move-left').on('mouseup', function()
        {
            if ($('.nao-move-left').attr('data-active'))
            {
                $.ajax({
                    type: "POST",
                    url: "../ajax/action",
                    dataType: "JSON",
                    data: {
                        'type_action': $('.nao-move-left').attr('data-action'),
                        'data-active': $('.nao-move-left').attr('data-active'),
                        'event': 'unpress'
                    },
                    success: function(data_result)
                    {
                        //TODO: Arreter de tourner à gauche
                        var texte = ' nao ne tourne plus à gauche';
                        $('.marcheplus').text(texte);
                    }
                });
                $('.nao-move-left').attr('data-active', false);
            }
        });
    });
}

function attach_event_action_sayanswer(e)
{//fonction ou nao repond a une question
    $(e).each(function()
    {
        $(e).attr('data-active', true);
        $.ajax({
            type: "POST",
            url: "../ajax/action",
            dataType: "JSON",
            data: {
                'type_action': $(e).attr('data-action'),
                'data-active': $(e).attr('data-active'),
                'id': $(e).attr('data-id'),
                'event': 'click'
            },
            success: function(data_result)
            {
                //TODO: Afficher la reponse de nao
                var texte = data_result['type_action'];
                $('.reponse').text(texte);
            }
        });
        $(e).attr('data-active', false);
    });
}

function attach_event_action(e)
{//fonction ou nao fait une action
    $(e).each(function()
    {
        $(e).attr('data-active', true);
        $.ajax({
            type: "POST",
            url: "../ajax/action",
            dataType: "JSON",
            data: {
                'type_action': $(e).attr('data-action'),
                'data-active': $(e).attr('data-active'),
                'event': 'click'
            },
            success: function(data_result)
            {
                //alert("coucou");
                //TODO: Afficher la reponse de nao
                var texte = data_result['type_action'];
                $('.action-simple').text(texte);
            }
        });
        $(e).attr('data-active', false);
    });
}

function setVolume(e)
{//fonction ou nao fait une action
    $(e).each(function()
    {
        $(e).attr('data-active', true);
        $.ajax({
            type: "POST",
            url: "../ajax/action",
            dataType: "JSON",
            data: {
                'type_action': $(e).attr('data-action'),
                'data-active': $(e).attr('data-active'),
                'value': $("#slider-vertical").slider("value"),
                'event': 'click'
            },
            success: function(data_result)
            {
                //TODO: Afficher la reponse de nao
                var texte = data_result['type_action'];
                $('.action-simple').text(texte);
            }
        });
        $(e).attr('data-active', false);
    });
}
