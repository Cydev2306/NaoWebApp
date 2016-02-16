<?php

class ColorpickerController extends Zend_Controller_Action {

    public function postDispatch() {
        $this->view->render('placeholder/menu.phtml');
    }

    public function init() {
        $auth = Zend_Auth::getInstance();
    }

    public function indexAction() {
        $this->redirect('/colorpicker/picker');
    }

    public function pickerAction() {
        if($this->getRequest()->isPost())
	{
         $cheminPython = APPLICATION_PATH . '/../python/';
         //exec('/usr/local/bin/python ' . $cheminPython . 'subCallLed.py', $output, $return);
         //$array['output'] = $output;
         //$array['return'] = $return;
         
        }
        /* if ($this->getRequest()->isPost())
          {
          /*$formConnexion = new Application_Form_Connexion();
          $this->view->formconnexion = $formConnexion;
          if($formConnexion->isValid($this->getRequest()->getPost()))
          {
          try
          {
          $couleur = $f->filter($formConnexion->getValue('couleur'));
          function extract_numbers($string)
          {
          preg_match_all('/([\d]+)/', $string, $match);
          return $match[0];
          }
          $numbers_array = extract_numbers($string);
          $log = new Logging();

          // set path and name of log file (optional)
          $log->lfile('mylog.txt');

          // write message to the log file
          $log->lwrite($numbers_array);
          // close log file
          $log->lclose();
          //$this->redirect('/colorpicker/picker');
          }
          catch(Zend_Exception $e)
          {
          Zend_Debug::dump($e);
          }
          }
          else
          {
          $this->view->erreur = 'Il y a eu une erreur avec la valeur';
          } */
        //}
    }
}
