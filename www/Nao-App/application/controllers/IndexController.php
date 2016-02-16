<?php

class IndexController extends Zend_Controller_Action
{
	public function postDispatch()
	{
		$this->view->render('placeholder/menu.phtml');
	}
	
    public function init()
    {
       $auth = Zend_Auth::getInstance();
       if (!$auth->hasIdentity())
       {
       		$this->redirect('/auth/login');
       }
    }

    public function indexAction()
    {

    }
    
    public function interfaceAction()
    {    	
    	$question = new Questionreponse();    	
    	$this->view->lesquestions = $question->selectAll();
    	$volume = new Sound();
    	$volumeActuel = $volume->selectVolume();
    	$this->view->volume = $volumeActuel[0]['volume'];
    }
}
