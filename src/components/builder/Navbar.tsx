import React from 'react';
import { Sparkles, Share2, Eye } from 'lucide-react';

export const Navbar = () => {
  return (
    <nav className="fixed top-0 w-full z-50 border-b border-white/10 bg-black/50 backdrop-blur-md px-6 py-4 flex justify-between items-center">
      <div className="flex items-center gap-2">
        <div className="w-8 h-8 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-lg flex items-center justify-center">
          <Sparkles className="text-white w-5 h-5" />
        </div>
        <span className="font-bold text-xl tracking-tight">CREATIVE UNLOCK <span className="text-indigo-500">AI</span></span>
      </div>
      
      <div className="flex items-center gap-4">
        <button className="flex items-center gap-2 px-4 py-2 hover:bg-white/5 rounded-full transition-all text-sm font-medium">
          <Eye size={18} /> Preview
        </button>
        <button className="flex items-center gap-2 bg-white text-black px-6 py-2 rounded-full font-bold text-sm hover:bg-indigo-50 transition-all shadow-[0_0_20px_rgba(255,255,255,0.3)]">
          <Share2 size={18} /> Instant Pitch
        </button>
      </div>
    </nav>
  );
};