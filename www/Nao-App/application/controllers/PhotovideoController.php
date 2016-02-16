<?php

class PhotovideoController extends Zend_Controller_Action
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
    	if(isset($_GET['nomImg']))
    	{
	    	$file = APPLICATION_PATH.'/../public/imgNao'.$_GET['nomImg'];
	    	$this->_helper->layout()->disableLayout();
	    	$this->_helper->viewRenderer->setNoRender(true);
	    	if (file_exists($file))
	    	{
	    		$uploadname=basename($file);

	    		// Envoi du fichier
	    		header('Content-Transfer-Encoding: none');
	    		header('Content-Type: application/force-download');
	    		header('Content-Disposition: attachment; filename="'.$uploadname.'"');
	    		header('Content-length: '.filesize($file));
	    		header("Pragma: no-cache");
	    		header("Cache-Control: must-revalidate, post-check=0, pre-check=0, public");
	    		header("Expires: 0");
	    		try{
	    			readfile($file) OR die();
	    		}catch(Zend_Exception $e){
	    			Zend_Debug::dump($e);
	    		}
	    	}
    	}
    	else
    	{
    		if(isset($_GET['nomVideo']))
    		{
    			$file = APPLICATION_PATH.'/../public/videoNao'.$_GET['nomVideo'];
    			$this->_helper->layout()->disableLayout();
    			$this->_helper->viewRenderer->setNoRender(true);
    			if (file_exists($file))
    			{
    				$uploadname=basename($file);

    				// Envoi du fichier
    				header('Content-Transfer-Encoding: none');
    				header('Content-Type: application/force-download');
    				header('Content-Disposition: attachment; filename="'.$uploadname.'"');
    				header('Content-length: '.filesize($file));
    				header("Pragma: no-cache");
    				header("Cache-Control: must-revalidate, post-check=0, pre-check=0, public");
    				header("Expires: 0");
    				try{
    					readfile($file) OR die();
    				}catch(Zend_Exception $e){
    					Zend_Debug::dump($e);
    				}
    			}
    		}
    	}
    }

    public function photoAction()
    {
    	$photo = new Photo();
    	$this->view->parquatre = $photo->getPremiere();
    }

    public function videoAction()
    {
    	$video = new Video();
    	$this->view->lesvideos = $video->selectAll();
    }

    public function supprimerphotoAction()
    {
    	if(isset($_GET['id']))
    	{
    		$photo = new Photo();
    		$selectlaphoto = $photo->selectOne($_GET['id']);
    		$photoname = $selectlaphoto['nomPhoto'];
    		exec('rm '.APPLICATION_PATH.'/../public/imgNao/'.$selectlaphoto['nomPhoto'],$output,$return);
    		$laphoto = $photo->find($_GET['id'])->current();
    		$laphoto->delete();
    		$this->_redirect('/photovideo/photo');
    	}
    }

    public function supprimervideoAction()
    {
    	if(isset($_GET['id']))
    	{
    		$video = new Video();
    		$selectlavideo = $video->selectOne($_GET['id']);
    		$videoname = $selectlavideo['nomVideo'];
    		exec('rm '.APPLICATION_PATH.'/../public/videoNao/'.$videoname.'.mp4',$outputmp4,$returnmp4);
    		exec('rm '.APPLICATION_PATH.'/../public/videoNao/miniature/'.$videoname.'.jpeg',$outputjpeg,$returnjpeg);

    		$lavideo = $video->find($_GET['id'])->current();
    		$lavideo->delete();
    		$this->_redirect('photovideo/video');
    	}
    }
}
