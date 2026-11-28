/* 회귀 테스트용 목 API — 실제 Issue #1 규모(댓글 1647개 · 17페이지) 흉내 */
(function(){
  var TOTAL=1647;
  var BASE=Date.parse('2026-11-18T10:40:34Z');
  var STEP=600000; /* 10분 간격 */
  var DELETED={};
  function mk(i){
    return {id:100000+i, user:{login:'soomonjjang-lab'}, created_at:new Date(BASE+i*STEP).toISOString(),
            updated_at:new Date(BASE+i*STEP).toISOString(), body:'[PC] 테스트 메시지 #'+i};
  }
  function allComments(){ var a=[]; for(var i=0;i<TOTAL;i++){ if(!DELETED[100000+i]) a.push(mk(i)); } return a; }
  function linkHdr(page,last){
    var parts=[];
    if(page<last) parts.push('<https://api.github.com/x?per_page=100&page='+(page+1)+'>; rel="next"');
    parts.push('<https://api.github.com/x?per_page=100&page=1>; rel="first"');
    parts.push('<https://api.github.com/x?per_page=100&page='+last+'>; rel="last"');
    return parts.join(', ');
  }
  function jsonRes(obj, headers){
    var h={'content-type':'application/json'};
    if(headers) for(var k in headers) h[k]=headers[k];
    return Promise.resolve(new Response(JSON.stringify(obj),{status:200,headers:h}));
  }

  window.__errs=[];
  window.addEventListener('error',function(e){ __errs.push('error: '+e.message); });
  window.addEventListener('unhandledrejection',function(e){ __errs.push('rejection: '+(e.reason&&(e.reason.message||JSON.stringify(e.reason)))); });

  window.__posted=[];
  window.mockAdd=function(txt){
    var i=TOTAL; TOTAL++;
    var c=mk(i);
    c.body=txt;
    c.updated_at=new Date().toISOString();
    window.__posted.push(c);
    return c;
  };

  var realFetch=window.fetch.bind(window);
  window.fetch=function(input, init){
    var url=typeof input==='string'?input:(input&&input.url);
    var u;
    try{ u=new URL(url); }catch(e){ return realFetch(input,init); }
    if(u.host!=='api.github.com') return realFetch(input,init);

    if(/\/issues\/1$/.test(u.pathname)){
      return jsonRes({number:1,comments:allComments().length});
    }
    var dm=u.pathname.match(/\/issues\/comments\/(\d+)$/);
    if(dm){ DELETED[parseInt(dm[1],10)]=1; return Promise.resolve(new Response(null,{status:204})); }

    if(/\/issues\/1\/comments$/.test(u.pathname)){
      if(init && init.method==='POST'){
        var body=JSON.parse(init.body||'{}');
        return jsonRes(mockAdd(body.body||''));
      }
      var per=parseInt(u.searchParams.get('per_page')||'30',10);
      var page=parseInt(u.searchParams.get('page')||'1',10);
      var since=u.searchParams.get('since');
      var items=allComments();
      if(since){
        var s=Date.parse(since);
        items=items.filter(function(c){ return Date.parse(c.updated_at)>s; });
      }
      var last=Math.max(1,Math.ceil(items.length/per));
      window.__reqLog=(window.__reqLog||[]);
      window.__reqLog.push({page:page,per:per,since:since||null,n:items.length,last:last});
      var slice=items.slice((page-1)*per,(page-1)*per+per);
      return jsonRes(slice,{'link':linkHdr(page,last)});
    }
    return jsonRes({});
  };

  try{ localStorage.setItem('pickle_chat_token_v1','TESTTOKEN'); }catch(e){}
})();
