import{h as v,b as N}from"./index-CS89oW_i.js";var M=typeof v=="object"&&v&&v.Object===Object&&v,B=M,D=B,U=typeof self=="object"&&self&&self.Object===Object&&self,H=D||U||Function("return this")(),w=H,X=w,q=X.Symbol,R=q,x=R,W=Object.prototype,z=W.hasOwnProperty,J=W.toString,l=x?x.toStringTag:void 0;function K(e){var t=z.call(e,l),i=e[l];try{e[l]=void 0;var a=!0}catch{}var c=J.call(e);return a&&(t?e[l]=i:delete e[l]),c}var Q=K,V=Object.prototype,Y=V.toString;function Z(e){return Y.call(e)}var ee=Z,I=R,te=Q,re=ee,ne="[object Null]",ie="[object Undefined]",E=I?I.toStringTag:void 0;function ae(e){return e==null?e===void 0?ie:ne:E&&E in Object(e)?te(e):re(e)}var oe=ae;function ce(e){return e!=null&&typeof e=="object"}var fe=ce,se=oe,ue=fe,be="[object Symbol]";function de(e){return typeof e=="symbol"||ue(e)&&se(e)==be}var me=de;function le(e){var t=typeof e;return e!=null&&(t=="object"||t=="function")}var $=le;const Me=N($);var ge=w,ve=function(){return ge.Date.now()},Te=ve,ye=/\s/;function je(e){for(var t=e.length;t--&&ye.test(e.charAt(t)););return t}var Se=je,$e=Se,Oe=/^\s+/;function pe(e){return e&&e.slice(0,$e(e)+1).replace(Oe,"")}var he=pe,_e=he,k=$,xe=me,G=NaN,Ie=/^[-+]0x[0-9a-f]+$/i,Ee=/^0b[01]+$/i,ke=/^0o[0-7]+$/i,Ge=parseInt;function Le(e){if(typeof e=="number")return e;if(xe(e))return G;if(k(e)){var t=typeof e.valueOf=="function"?e.valueOf():e;e=k(t)?t+"":t}if(typeof e!="string")return e===0?e:+e;e=_e(e);var i=Ee.test(e);return i||ke.test(e)?Ge(e.slice(2),i?2:8):Ie.test(e)?G:+e}var Ne=Le,we=$,S=Te,L=Ne,Re="Expected a function",We=Math.max,Ce=Math.min;function Pe(e,t,i){var a,c,u,s,n,f,b=0,O=!1,d=!1,T=!0;if(typeof e!="function")throw new TypeError(Re);t=L(t)||0,we(i)&&(O=!!i.leading,d="maxWait"in i,u=d?We(L(i.maxWait)||0,t):u,T="trailing"in i?!!i.trailing:T);function y(r){var o=a,m=c;return a=c=void 0,b=r,s=e.apply(m,o),s}function C(r){return b=r,n=setTimeout(g,t),O?y(r):s}function P(r){var o=r-f,m=r-b,_=t-o;return d?Ce(_,u-m):_}function p(r){var o=r-f,m=r-b;return f===void 0||o>=t||o<0||d&&m>=u}function g(){var r=S();if(p(r))return h(r);n=setTimeout(g,P(r))}function h(r){return n=void 0,T&&a?y(r):(a=c=void 0,s)}function A(){n!==void 0&&clearTimeout(n),b=0,a=f=c=n=void 0}function F(){return n===void 0?s:h(S())}function j(){var r=S(),o=p(r);if(a=arguments,c=this,f=r,o){if(n===void 0)return C(f);if(d)return clearTimeout(n),n=setTimeout(g,t),y(f)}return n===void 0&&(n=setTimeout(g,t)),s}return j.cancel=A,j.flush=F,j}var Ae=Pe;const Be=N(Ae);export{oe as _,$ as a,w as b,R as c,Be as d,fe as e,Me as f,B as g,Ae as h,me as i,Ne as t};
