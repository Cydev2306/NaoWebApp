<?php
class Video extends Zend_Db_Table_Abstract
{
	protected $_name='video';
	protected $_primary=array('idVideo');
	
	public function selectAll()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete ='SELECT * FROM video WHERE transcoder = 1 ORDER BY idVideo DESC';
		return $db->query($requete)->fetchAll();
	}
	
	public function selectOne($id)
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this)->where('idVideo='.$id);
		return $db->query($requete)->fetch();
	}
	
	public function getIdMax()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT MAX(idVideo) FROM video';
		return $db->query($requete)->fetch();
	}
	
	public function updateConvert($nom,$etat)
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'UPDATE video SET transcoder='.$etat.' WHERE nomVideo="'.$nom.'"';
		return $db->query($requete)->fetch();
	}
	
	public function selectVideoNonFormatées()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT * FROM video WHERE transcoder = 0';
		return $db->query($requete)->fetchAll();
	}
	
	public function getPremiere()
	{	//retourne les 4 dernieres videos
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT * FROM video ORDER BY idVideo DESC LIMIT 0,4';
		return $db->query($requete)->fetchAll();
	}
	
	public function getQuatre($last)
	{	//retourne la suite des videos en appel ajax
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT * FROM video WHERE idPhoto < '.$last.' ORDER BY idVideo DESC LIMIT 0,4';
		return $db->query($requete)->fetchAll();
	}
}