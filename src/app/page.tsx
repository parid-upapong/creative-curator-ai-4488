'use client';
import React, { useState, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Navbar } from '@/components/builder/Navbar';
import { AISidebar } from '@/components/builder/AISidebar';
import { Upload, Plus, LayoutGrid, Image as ImageIcon, Loader2 } from 'lucide-react';

export default function PortfolioBuilder() {
  const [assets, setAssets] = useState<any[]>([]);
  const [isDragging, setIsDragging] = useState(false);

  const simulateAIAnalysis = (newAssetId: string) => {
    setTimeout(() => {
      setAssets(prev => prev.map(asset => 
        asset.id === newAssetId 
          ? { 
              ...asset, 
              status: 'completed', 
              aiMetadata: { 
                tags: ['Minimalist', 'Corporate-Modern', 'High-Contrast'],
                style: 'Bauhaus Tech',
                scores: { technical: 94, commercial: 88, innovation: 82 }
              } 
            } 
          : asset
      ));
    }, 2500);
  };

  const handleFileUpload = (e: any) => {
    const id = Math.random().toString(36).substr(2, 9);
    const newAsset = {
      id,
      url: URL.createObjectURL(e.target.files[0]),
      status: 'analyzing',
      type: 'image'
    };
    setAssets([...assets, newAsset]);
    simulateAIAnalysis(id);
  };

  return (
    <main className="flex flex-col h-screen pt-16">
      <Navbar />
      
      <div className="flex flex-1 overflow-hidden">
        {/* Main Canvas */}
        <div className="flex-1 overflow-y-auto bg-[#050505] p-12">
          <div className="max-w-4xl mx-auto">
            <header className="mb-12">
              <input 
                type="text" 
                placeholder="Untitled Portfolio" 
                className="bg-transparent text-4xl font-bold outline-none border-none placeholder:text-white/10 w-full"
              />
              <p className="text-gray-500 mt-2">AI-Powered Rapid Portfolio Builder v1.0</p>
            </header>

            <div className="grid grid-cols-2 gap-6">
              <AnimatePresence>
                {assets.map((asset) => (
                  <motion.div
                    key={asset.id}
                    layout
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    className="relative group aspect-video glass-panel overflow-hidden border-2 border-transparent hover:border-indigo-500/50 transition-all"
                  >
                    <img src={asset.url} className="w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity" />
                    
                    {asset.status === 'analyzing' && (
                      <div className="absolute inset-0 flex flex-col items-center justify-center bg-black/60 backdrop-blur-sm">
                        <Loader2 className="animate-spin text-indigo-500 mb-2" />
                        <span className="text-[10px] uppercase tracking-widest text-indigo-400 font-bold">AI Standardizing...</span>
                      </div>
                    )}
                  </motion.div>
                ))}
              </AnimatePresence>

              <label className="cursor-pointer border-2 border-dashed border-white/10 rounded-xl aspect-video flex flex-col items-center justify-center hover:bg-white/5 hover:border-white/20 transition-all group">
                <input type="file" className="hidden" onChange={handleFileUpload} />
                <div className="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center group-hover:scale-110 transition-transform">
                  <Plus className="text-gray-400" />
                </div>
                <span className="mt-4 text-sm text-gray-500 font-medium">Add Creative Asset</span>
                <span className="text-[10px] text-gray-600 mt-1 uppercase">Supports JPG, PNG, MP4</span>
              </label>
            </div>
          </div>
        </div>

        {/* AI Control Panel */}
        <AISidebar assets={assets} />
      </div>
    </main>
  );
}