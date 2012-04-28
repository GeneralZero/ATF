package bridings;

public class myBST {
    public class BSTNode {
        public Object data;
        public BSTNode lc;
        public BSTNode rc;
        public BSTNode(){
            data = null;
            lc=null;
            rc=null;
        }
        public BSTNode(Object o){
            data = o;
            lc=null;
            rc=null;
        }
        @Override
        public String toString(){
            String ret = "";
            if(root.data !=null)
                ret.concat(root.data.toString());
            if(root.lc !=null)
                ret.concat(root.lc.toString());
            if(root.rc !=null)
                ret.concat(root.rc.toString());
            return ret;
        }
    }
    private BSTNode root;

    public int hight(){
        return hight(root);
    }

    public Object remove(Comparable k){
        if((k!=null)&&(root!=null)){
            BSTNode ret = new BSTNode();
            root=remove(root,k,ret);
            if(ret.data!=null){
                return ret.data;
            }
        }
        return null;
    }
    public Object find(Comparable o){
        if(o!= null){
            return find(root, o);
        }
        return null;
    }
    public boolean add(Comparable o){
        if(o== null)
            return false;
        else{
            root= add(root, o);
            return true;
        }
    }
    private int hight(BSTNode sr){
        if(sr==null)
            return 0;
        return 1 + MAX(hight(sr.lc), hight(sr.rc));
    }

    private int MAX(int a, int b){
        if(a>b)
            return a;
        return b;
    }

    private Object find(BSTNode sr, Comparable k){
        if(sr ==null)
            return null;
        if(k.compareTo(sr.data) == 0)
            return sr.data;
        if(k.compareTo(sr.data)<0)
            return find(sr.lc,k);
        return find(sr.rc, k);
    }
    private BSTNode remove(BSTNode sr, Comparable k, BSTNode ret){
        Object temp = null;
        if(sr!= null){
            if(k.compareTo(sr.data)< 0)
                sr.lc=remove(sr.lc, k, ret);
            if(k.compareTo(sr.data) > 0)
                sr.rc = remove(sr.lc, k, ret);
            else{
                ret.data = sr.data;
                if(sr.lc == null)
                    return sr.rc;
                if(sr.rc == null)
                    return sr.lc;
                temp = ret.data;
                sr.rc = removeMin(sr.rc, ret);
                sr.data = ret.data;
                ret.data = temp;
            }
        }
        return sr.lc;
    }
    private BSTNode removeMin(BSTNode sr, BSTNode ret){
        if(sr.lc == null){
            ret.data = sr.data;
            return sr.rc;
        }
        sr.lc = removeMin(sr.lc, ret);
        return sr;
    }
    private BSTNode add(BSTNode sr, Comparable o){
        if(sr == null)
            return new BSTNode(o);
        if(o.compareTo(sr.data) < 0)
            sr.lc = add(sr.lc, o);
        else
            sr.rc = add(sr.rc,o);
        return sr;
    }
}
