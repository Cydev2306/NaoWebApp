<?php
class Questionreponse extends Zend_Db_Table_Abstract
{
	protected $_name='questionreponse';
	protected $_primary=array('id');
	
	public function selectAll()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this);
		return $db->query($requete)->fetchAll();
	}
	
	public function selectOne($id)
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = $this->select()->from($this)->where('id='.$id);
		return $db->query($requete)->fetch();
	}
	
	public function getIdMax()
	{
		$db = Zend_Db_Table::getDefaultAdapter();
		$requete = 'SELECT MAX(id) FROM questionreponse';
		return $db->query($requete)->fetch();
	}
}