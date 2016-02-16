<?php
class NaoviewController extends Zend_Controller_Action
{
	public function init()
	{
		$auth = Zend_Auth::getInstance();
		/*if (!$auth->hasIdentity())
		{
			$this->redirect('/auth/login');
		}*/
	}

	public function indexAction()
	{
		$this->_helper->layout->setLayout('layout_naoview');
	}
	
	public function postDispatch()
	{
		$this->view->render('placeholder/menu.phtml');
	}
}
