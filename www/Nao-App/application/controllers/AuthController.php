<?php

class AuthController extends Zend_Controller_Action {

    function logoutAction() {
        Zend_Auth::getInstance()->clearIdentity();
        $this->_redirect('index/index');
    }

    public function loginAction() {
        $this->_helper->layout->setLayout('layout_connexion');
        $formConnexion = new Application_Form_Connexion();
        $this->view->formconnexion = $formConnexion;
        $auth = Zend_Auth::getInstance();
        if ($auth->hasIdentity()) {
            $this->redirect('/index/index');
        } else {
            if ($this->getRequest()->isPost()) {
                if ($formConnexion->isValid($this->getRequest()->getPost())) {
                    try {
                        $f = new Zend_Filter_StripTags();
                        $login = $f->filter($formConnexion->getValue('login'));
                        $password = $f->filter($formConnexion->getValue('motDePasse'));
                        //charger et parametrer l'adapteur
                        //on peut passer un dernier parametre 'MD5(?)'
                        $dbAdapter = new Zend_Auth_Adapter_DbTable(Zend_Db_Table::getDefaultAdapter(), 'user', 'login', 'motDePasse');

                        //charger les logs à vérifier
                        $dbAdapter->setIdentity($login);
                        $dbAdapter->setCredential($password);

                        //on test l'autentification
                        $resultat = $auth->authenticate($dbAdapter);

                        if ($resultat->isValid()) {
                            $Utilisateur_Session_Namespace = new Zend_Session_Namespace("Utilisateur");
                            $Utilisateur_Session_Namespace->Utilisateur = $this->getRequest()->getPost();
                            $this->redirect("/index/index");
                        }
                    } catch (Zend_Exception $e) {
                        Zend_Debug::dump($e);
                    }
                } else {
                    $this->view->erreur = 'Login ou mot de passe non valide';
                }
            }
        }
    }

}
