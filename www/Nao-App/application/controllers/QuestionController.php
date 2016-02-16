<?php

class QuestionController extends Zend_Controller_Action
{
	public function postDispatch()
	{
		$this->view->render('placeholder/menu.phtml');
	}

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
		 $question = new Questionreponse();
		 $this->view->lesquestions = $question->selectAll();
	}
	
	public function ajoutAction()
	{
		$formAjoutQuestion = new Application_Form_Questionreponse();
		$this->view->formajoutquestion = $formAjoutQuestion;
		if($this->getRequest()->isPost())
		{
			$data = $this->getRequest()->getPost();
			if($formAjoutQuestion->isValid($data))
			{
				$question= new Questionreponse();
				$max = $question->getIdMax();
				$newQuestion = $question->createRow();
				$newQuestion->id = $max["MAX(id)"]+1;
				$newQuestion->question = $formAjoutQuestion->getValue('question');
				$newQuestion->reponse = $formAjoutQuestion->getValue('reponse');
				$newQuestion->save();
				
				$this->_redirect('question/index');
			}
			else
			{
				$this->view->formajoutquestion = $formAjoutQuestion;
			}
		}
	}
	
	public function supprimerAction()
	{
		if(isset($_GET['id']))
		{
			$question = new Questionreponse();
    		$laquestion = $question->find($_GET['id'])->current();
    		$laquestion->delete();
			$this->_redirect('question/index');
		}
	}
}
